# Portfolio
학교, 데이콘, 캐글에서 진행한 프로젝트 코드들
https://www.kaggle.com/kkj214


## 1. Project - LG / 시스템 품질 변화로 인한 사용자 불편 예지 AI 경진대회
https://dacon.io/competitions/official/235687/overview/description
### 배경 :  
- 다양한 장비/서비스에서 일어나는 시스템 데이터를 통해 사용자의 불편을 예지하기 위해 ‘시스템 데이터’와 ‘사용자 불편 발생 데이터’를 분석하여 불편을 느낀 사용자와 불편 요인들을 찾아주세요.


### 목적 :
- 데이터를 통해 사용자가 불편을 느끼는 원인 분석


### Summary :
#### (1). Data Collection
- 학습(Train) 데이터(시스템에 발생한 에러 로그 + 시스템 퀄리티 로그 + 사용자 불만&불만이 접수된 시간) + 테스트(Test) 데이터(에러 로그 + 퀄리티 로그 + 사용자 불만 확률) 
#### (2). Data Preprocessing
- EDA (에러 로그 데이터 + 시스템 퀄리티 데이터)
- Reduction (중복 데이터 제거, missing value 포함한 결측치 제거)
#### (3). Model & Algorithms
- lgb, xgb, gb 모델로 피팅 
#### (4). Report & Review
- 피드백 : 모델링 부분은 어떤 모델이 제일 나은지 불확실한것 같음
- 변수 파악이 쉽지 않아 전처리 부분에서도 어려움을 겪음
