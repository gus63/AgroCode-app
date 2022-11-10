from flask import Flask
# from flask import Flask, Blueprint
# from flask_bootstrap import Bootstrap
# from flask_login import LoginManager
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy

app = Flask("app")
# app.secret_key = '12QwrT!'
# auth = Blueprint('auth', __name__)
# для portainer BD-->
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://admin:admin1234@postgres:5432/postgres"
# app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)
# для локальной BD -->
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin1234@localhost:5432/postgres"
# manager = LoginManager(app)
# manager.login_view = 'auth.login'
# bootstrap = Bootstrap(app)


@app.route('/', methods=['GET'])
def home():
    return 'hello !!!!'

# from sweater import models, routes