from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate

app = Flask(__name__)
auth = Blueprint('auth', __name__)
app.secret_key = '12QwrT!'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin1234@postgres:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)

#from sweater.models import Role, User

#with app.app_context():
#    db.drop_all()
#    db.create_all()
#    db.session.commit()

from sweater import models, routes

migrate = Migrate(app, db)
manager = LoginManager(app)
manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)
