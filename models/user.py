from .db import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, username=None, password=None, is_active=True):
        self.username = username
        self.password = password
        self.is_active = is_active
