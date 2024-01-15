import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("PG_USER")
DB_PSWD = os.getenv("PG_PASSWORD")
DB_NAME = os.getenv("PG_DBNAME")
DB_HOST = os.getenv("PG_HOST")

class Config:
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PSWD}@localhost:5432/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATION = False

config = {
    'development': DevelopmentConfig
}