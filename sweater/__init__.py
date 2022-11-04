from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
auth = Blueprint('auth', __name__)
app.secret_key = '12QwrT!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin1234@postgresql:5432/test'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)
manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)

from sweater import models, routes

db.create_all()