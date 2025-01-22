from .db import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    lecture_id = db.Column(db.Integer, db.ForeignKey('lecture.id'), nullable=False)
    description = db.Column(db.String(128), nullable=False)
    deadline = db.Column(db.DateTime, nullable=False)