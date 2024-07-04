# main.py
from config import db_config

db_name = db_config['name']
db_user = db_config['user']
db_password = db_config['password']
db_host = db_config['host']

# Example of using these credentials to connect to MySQL
import mysql.connector

connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
)

cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
record = cursor.fetchone()
print("You're connected to database: ", record)
