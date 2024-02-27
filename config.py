from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI_DATAWAREHOUSE = os.getenv("DATABASE_URL_DATAWAREHOUSE")
    SQLALCHEMY_DATABASE_URI_STAGING = os.getenv("DATABASE_URL_STAGING")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
