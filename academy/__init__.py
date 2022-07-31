from flask import Flask, url_for
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AcademyDatabase/academy.db'
app.config['SECRET_KEY'] = 'c04be6db67e77e45c8feacf9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_user_route'
login_manager.login_message_category = 'warning'

from academy import routes
