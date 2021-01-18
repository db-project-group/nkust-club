import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = ""
    SECRET_KEY = os.urandom(24)
    JWT_SECRET_KEY = os.urandom(24)