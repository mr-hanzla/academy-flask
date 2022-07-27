from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///AcademyDatabase/academy.db'
app.config['SECRET_KEY'] = 'c04be6db67e77e45c8feacf9'
db = SQLAlchemy(app)

from academy import routes
