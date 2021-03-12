import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_GET') or 'let-me-be-one-with-everything-1-!'
