from flask import Flask
from suade_app.config import Config
from flask_sqlalchemy import SQLAlchemy
import psycopg2 as pg

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config.from_object(Config)

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="interview",pw="uo4uu3AeF3",url="candidate.suade.org", db="suade")
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["CACHE_TYPE"] = "null"
engine = create_engine(DB_URL, convert_unicode=True)

con = engine.connect()

from suade_app import routes
