from .db import db

class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    week = db.Column(db.String(80), nullable=False)
    timetable = db.Column(db.Integer, nullable=False)