import pandas as pd
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator
from nba_api.stats.endpoints import leaguedashplayerstats, drafthistory

# Spark 세션 생성
spark = SparkSession.builder.appName("NBA Rookie Prediction").getOrCreate()

# 신인 선수 데이터를 가져오기 위한 함수
def get_rookie_data(season):
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(season=season).get_data_frames()[0]
    draft_stats = drafthistory.DraftHistory().get_data_frames()[0]
    rookies = draft_stats[draft_stats['SEASON'] == season[:4]]
    rookie_stats = player_stats[player_stats['PLAYER_ID'].isin(rookies['PERSON_ID'])]
    return rookie_stats

# 모델 학습 함수
def train_model():
    rookie_data_2022 = get_rookie_data('2022-23')
    rookie_of_the_year_df = pd.read_csv('data/rookie_of_the_year.csv')
    data = {
        'PLAYER_NAME': rookie_data_2022['PLAYER_NAME'],
        'POINTS': rookie_data_2022['PTS'],
        'ASSISTS': rookie_data_2022['AST'],
        'REBOUNDS': rookie_data_2022['REB'],
        'ROOKIE_OF_THE_YEAR': [1 if name in rookie_of_the_year_df['PLAYER_NAME'].values else 0 for name in rookie_data_2022['PLAYER_NAME']]
    }
    df = pd.DataFrame(data)
    
    # Pandas 데이터프레임을 Spark 데이터프레임으로 변환
    spark_df = spark.createDataFrame(df)
    
    # 특징 벡터를 만들기 위한 VectorAssembler 사용
    assembler = VectorAssembler(inputCols=['POINTS', 'ASSISTS', 'REBOUNDS'], outputCol='features')
    assembled_df = assembler.transform(spark_df)
    
    # 데이터 분리
    train_df, test_df = assembled_df.randomSplit([0.8, 0.2], seed=42)
    
    # RandomForestClassifier 모델 생성 및 학습
    rf = RandomForestClassifier(labelCol='ROOKIE_OF_THE_YEAR', featuresCol='features', numTrees=100, seed=42)
    model = rf.fit(train_df)
    
    # 모델 평가
    predictions = model.transform(test_df)
    evaluator = MulticlassClassificationEvaluator(labelCol='ROOKIE_OF_THE_YEAR', predictionCol='prediction', metricName='accuracy')
    accuracy = evaluator.evaluate(predictions)
    print(f'모델 정확도: {accuracy * 100:.2f}%')
    
    return model

# 예측 함수
def predict_rookie_of_the_year(model, season):
    rookie_data = get_rookie_data(season)
    new_data = {
        'PLAYER_NAME': rookie_data['PLAYER_NAME'],
        'POINTS': rookie_data['PTS'],
        'ASSISTS': rookie_data['AST'],
        'REBOUNDS': rookie_data['REB']
    }
    df = pd.DataFrame(new_data)
    spark_df = spark.createDataFrame(df)
    
    assembler = VectorAssembler(inputCols=['POINTS', 'ASSISTS', 'REBOUNDS'], outputCol='features')
    assembled_df = assembler.transform(spark_df)
    
    predictions = model.transform(assembled_df)
    predictions = predictions.select('PLAYER_NAME', 'POINTS', 'ASSISTS', 'REBOUNDS', 'probability', 'prediction')
    
    # 예측 결과를 Pandas 데이터프레임으로 변환
    result_df = predictions.toPandas()
    result_df['PROBABILITY'] = result_df['probability'].apply(lambda x: x[1] * 100)
    
    top_candidates = result_df.sort_values(by='PROBABILITY', ascending=False).head(5)
    return top_candidates
