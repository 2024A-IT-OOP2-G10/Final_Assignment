from peewee import Model,CharField, IntegerField, DateField
from .db import db

class User(Model): 
    user_id = CharField()
    password = CharField()

    class Meta:
        database = db
