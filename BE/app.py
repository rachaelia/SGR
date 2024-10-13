import psycopg2
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from nltk.sentiment import SentimentIntensityAnalyzer

from config import load_config
from connect import connect

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['POST'])
@cross_origin()
def analyze_emotion():
    if request.method == 'POST':
        text = str(request.json.get('input_text')).lower()
        connection = get_connection()
        cursor = connection.cursor()
        result = None
        try:
            cursor.execute('SELECT compound FROM sentiment_registry where input = (%s);', (text,))
            query_result = cursor.fetchone()
            if query_result is not None:
                result = compute_sentiment(query_result[0])
            else:
                compound = get_compound(text)
                result = compute_sentiment(compound)
                cursor.execute(
                    'INSERT INTO sentiment_registry (input, compound) VALUES (%s, %s)',
                    (text, compound)
                )
        except psycopg2.Error as error:
            print('Unable to execute query!\n{0}'.format(error))
        finally:
            connection.close()

        return jsonify(result)


def compute_sentiment(compound):
    if compound > 0:
        return 'Positive sentiment'
    elif compound < 0:
        return 'Negative sentiment'
    else:
        return 'Neutral sentiment'


def get_connection():
    config = load_config()
    connection = connect(config)
    connection.autocommit = True
    return connection


def get_compound(text):
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text).get('compound')


if __name__ == '__main__':
    #    app.run(debug=True)
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
