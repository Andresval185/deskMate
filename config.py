import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'deskmate-secret-key-2025'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://deskmate:deskmate123@localhost/deskmate'
    SQLALCHEMY_TRACK_MODIFICATIONS = False