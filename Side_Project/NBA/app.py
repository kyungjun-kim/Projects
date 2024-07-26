from flask import Flask, render_template, request
import model

app = Flask(__name__)

# 메인 페이지
@app.route('/')
def index():
    return render_template('index.html')

# 예측 결과 페이지
@app.route('/predict', methods=['POST'])
def predict():
    season = request.form['season']
    trained_model = model.train_model()
    predictions = model.predict_rookie_of_the_year(trained_model, season)
    return render_template('result.html', season=season, predictions=predictions)

if __name__ == '__main__':
    app.run(debug=True)
