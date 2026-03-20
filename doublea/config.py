import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DOUBLEA_DATABASE_URI')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT= 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('USER_EMAIL')
    MAIL_PASSWORD = os.environ.get('USER_PASS')
    MAIL_DEFAULT_SENDER = 'naitinchina@gmail.com'
