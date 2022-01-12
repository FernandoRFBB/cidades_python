import os
from dotenv import load_dotenv
import pyodbc

load_dotenv()

server = str(os.getenv("DB_HOST"));
database = str(os.getenv("DB_DATABASE"));
username = str(os.getenv("DB_USERNAME"));
password = str(os.getenv("DB_PASSWORD"));

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password);
cursor = conn.cursor();
