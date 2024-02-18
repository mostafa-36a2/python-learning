from base import create_app, db
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy


class User(UserMixin, db.Model):
    """
    Simple model
    """

    id = db.Column(
        db.Integer, primary_key=True
    )  # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
