import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv(override=True)

def get_connected():
    connection=mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    return connection

# connection=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     database="job_tracker"
# )
# print("MySQL connected successfully!")
# connection.close()

# def get_connected():
#     connection=mysql.connector.connect(
#         host="localhost",
#         user="root",   
#         database="job_tracker"
#     )
#     return connection