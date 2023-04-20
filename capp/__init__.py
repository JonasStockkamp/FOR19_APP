from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

application = Flask(__name__)

### Code GitHub
application.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
DBVAR=os.environ['DATABASE_URL']
DBVAR="postgresql://qlxkwdsnkawsbm:1ca7aed214c057c14625c63ebb0c6b26b46c697d23d647873b41cd5ebd46f19a@ec2-34-241-82-91.eu-west-1.compute.amazonaws.com:5432/d8gk37k9bg36kl"
DBVAR="postgresql://username:password@host:port/database"
application.config['SQLALCHEMY_DATABASE_URI'] = DBVAR 
application.config['SQLALCHEMY_BINDS'] ={'transport': DBVAR}

db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager= LoginManager(application)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app
from capp.users.routes import users

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
application.register_blueprint(users)

