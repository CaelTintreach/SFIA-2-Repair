from flask import Flask
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
import os

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
#app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes