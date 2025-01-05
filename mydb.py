from dotenv import load_dotenv
import mysql.connector
import os

# Load environment variables from .env file
load_dotenv()

dataBase = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASS'),
)
# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute(f"CREATE DATABASE {os.getenv('DB_NAME')}")

print("All Done!")
