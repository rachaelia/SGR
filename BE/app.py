import psycopg2
import logging
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
    """
    Checks if the input text received from the client is already present in the DB,
    if so it returns the stored output value otherwise computes the sentiment and
    saves the new row in the DB
    :return: The result of the sentiment analysis as a JSON
    """
    if request.method == 'POST':
        text = str(request.json.get('input_text')).lower()
        connection = get_connection()
        cursor = connection.cursor()
        result = None
        compound = 0
        try:
            cursor.execute('SELECT sentiment FROM sentiment_registry where input = (%s);', (text,))
            query_result = cursor.fetchone()
            if query_result is not None:
                result = query_result
            else:
                compound = get_compound(text)
                result = compute_sentiment(compound)
            cursor.execute(
                'INSERT INTO sentiment_registry (input, compound, sentiment) VALUES (%s, %s, %s)',
                (text, compound, result)
            )
        except psycopg2.Error as error:
            logging.error('Unable to execute query!\n{0}'.format(error))
        finally:
            cursor.close()
            connection.close()
        return jsonify(result)


def compute_sentiment(compound):
    """
    Evaluates the compound value and returns the sentiment
    :param compound
    :return: The sentiment evaluation
    """
    if compound > 0:
        return 'Positive sentiment'
    elif compound < 0:
        return 'Negative sentiment'
    else:
        return 'Neutral sentiment'


def get_connection():
    """
    Performs the connection to the PostgreSQL database
    :return: The connection
    """
    config = load_config()
    connection = connect(config)
    connection.autocommit = True
    return connection


def get_compound(text):
    """
    Uses the SentimentIntensityAnalyzer of Natural Language Toolkit library to evaluates text
    :param str text: input text received from the client\
    :return: the resulting compound value
    """
    sia = SentimentIntensityAnalyzer()
    return sia.polarity_scores(text).get('compound')


def create_app():
    """
    :return: the app instance used by the waitress-serve command in the Dockerfile
    """
    return app
