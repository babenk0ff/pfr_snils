import os


class Config:
    DEBUG = True
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.getcwd()}/test_db.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ALLOWED_EXTENSIONS = {'txt'}
