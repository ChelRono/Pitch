from crypt import methods
from turtle import title
from unicodedata import category
import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
app.config['SECRET_KEY']='12345'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
login_manager= LoginManager(app)
bcrypt=Bcrypt(app)



from app.main import views
