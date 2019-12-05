from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from os import getenv
from flask_login import LoginManager
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + getenv('MY_SQL_USER') + ':' + getenv('MY_SQL_PASS') + '@' + getenv('MY_SQL_HOST') + '/' + getenv('MY_SQL_DB')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

app.config['SECRET_KEY'] = getenv('KEY')

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from front import routes
