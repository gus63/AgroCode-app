from flask import Flask, Blueprint
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object(config)
auth = Blueprint('auth', __name__)
app.secret_key = '12QwrT!'
# для portainer BD-->
#app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin1234@postgres:5432/postgres"
# для локальной BD -->
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin1234@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
manager = LoginManager(app)
manager.login_view = 'auth.login'
bootstrap = Bootstrap(app)

with app.app_context():
    db.create_all()

from sweater import models, routes