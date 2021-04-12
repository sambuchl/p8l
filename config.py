import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    ADMINS = ['support@skunkl.com']

    LANGUAGES = ['en', 'es']

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    POSTS_PER_PAGE = 25

    SECRET_KEY = os.environ.get('SECRET_GET') or 'let-me-be-one-with-everything-1-!'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
