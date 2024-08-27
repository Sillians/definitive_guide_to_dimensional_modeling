import psycopg2
from psycopg2 import Error
from dotenv import load_dotenv

import logging
from logger import *
import settings as setting

load_dotenv()
log = Logger("Connection to PostgreSQL Database", logging.INFO).get_logger()

def connect_database():
    """
    Create a connection to the database
    using the environment variables
    """
    try:
        log.info("Connect to an existing database")
        connection = psycopg2.connect(
            user=setting.DATABASE_USER,
            password=setting.DATABASE_PASSWORD,
            host=setting.DATABASE_HOST,
            port=setting.DATABASE_PORT,
            database=setting.DATABASE_NAME,
        )

        log.info("Create a cursor to perform database operations")
        cursor = connection.cursor()
        log.info("Connection to database established")

    except (Exception, Error) as error:
        log.info("Error while connecting to PostgreSQL", error)

    return connection, cursor
