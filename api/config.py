import os
from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv("PG_USER")
DB_PASSWD = os.getenv("PG_PASSWORD")
DB_NAME = os.getenv("PG_DBNAME")
DB_HOST = os.getenv("PG_HOST")
DB_PORT = os.getenv("PG_PORT")
DB_NAME_TEST = os.getenv("DBNAME_TEST")


class Config:
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATION = False


class TestConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME_TEST}"
    SQLALCHEMY_TRACK_MODIFICATION = False


config = {
    'test': TestConfig,
    'development': DevelopmentConfig
}
