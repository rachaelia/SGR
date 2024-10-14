import psycopg2
import logging
from config import load_config

def connect(config):
    """ Connect to the PostgreSQL database server """
    try:
        with psycopg2.connect(**config) as conn:
            if conn is not None:
                logging.info('Connected successfully')
                return conn
    except (psycopg2.DatabaseError, Exception) as error:
        logging.error(error)


if __name__ == '__main__':
    config = load_config()
    connect(config)