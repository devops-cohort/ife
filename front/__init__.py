from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + getenv('MY_SQL_USER') + ':' + getenv('MY_SQL_PASS')
 + '@' + getenv('MY_SQL_HOST') + '/' + getenv('MY_SQL_DB')

db = SQLAlchemy(app)

app.config['SECRET_KEY'] = getenv('KEY')

from front import route
