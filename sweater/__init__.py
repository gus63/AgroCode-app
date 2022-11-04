from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from sweater import models, routes


app = Flask(__name__)
auth = Blueprint('auth', __name__)
app.secret_key = '12QwrT!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin1234@postgres:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)
manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)

db.create_all()
