import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'my_name_ifti_khan'
    SQLALCHEMY_DATABASE_URI = "mssql+pyodbc://localhost\\SQLEXPRESS/MTM?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_MIGRATE_DIR = "migrations"
    SQLALCHEMY_ECHO = True  
    
