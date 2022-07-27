from flask_sqlalchemy import SQLAlchemy
from academy import db

class PostTesting(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)