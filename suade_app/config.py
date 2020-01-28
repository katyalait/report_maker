import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_password'
    POSTGRES_URL = os.environ.get('POSTGRES_URL') or 'candidate.suade.org'
    POSTGRES_USER = os.environ.get('POSTGRES_USER') or 'interview'
    POSTGRES_PW = os.environ.get('POSTGRES_PW') or "uo4uu3AeF3"
    POSTGRES_DB = os.environ.get('POSTGRES_DB') or 'suade'
