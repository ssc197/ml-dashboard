from flask import Flask, jsonify, request
from flask_cors import CORS
from models.sentiment_analysis import checkTheSentiment


# creating the flask app

app = Flask(__name__)
CORS(app)



@app.route('/sentiment-analysis',methods=['POST'])
def analyze_sentiment():
    query = request.get_json()
    text = query['analysis_query']
    senti = checkTheSentiment(text)
    return jsonify(senti)


if __name__ == '__main__':
	app.run(debug="true")