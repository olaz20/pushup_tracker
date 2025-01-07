from . import db
from flask_login import UserMixin
from datetime import datetime, timezone

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))
    workout = db.relationship('Workout', backref='author', lazy=True)

class Workout(db.Model):
    __tablename__ = 'workout'
    id = db.Column(db.Integer, primary_key=True)
    pushups = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    comment = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
