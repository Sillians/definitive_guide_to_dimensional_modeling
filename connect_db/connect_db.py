import psycopg2
from psycopg2 import Error

import os
from dotenv import load_dotenv
load_dotenv()

try:
    # Connect to an existing database
    connection = psycopg2.connect(user=os.getenv('DATABASE_USER'),
                                  password=os.getenv('DATABASE_PASSWORD'),
                                  host=os.getenv('DATABASE_HOST'),
                                  port=os.getenv('DATABASE_PORT'),
                                  database=os.getenv('DATABASE_NAME'))
    
    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")
    # Fetch all result (retrieve query result using cursor methods)
    record_all = cursor.fetchall() 
    print("You are connected to all result - ", record_all, "\n")
    # Fetch many result (retrieve query result using cursor methods)
    record_many = cursor.fetchmany() 
    print("You are connected to many results -", record_many, "\n")
    
except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
        