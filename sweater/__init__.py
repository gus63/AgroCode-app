from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap


app = Flask(__name__)
auth = Blueprint('auth', __name__)
app.secret_key = '12QwrT!'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin1234@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = LoginManager(app)
manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)

db.create_all()


from sweater import models, routes