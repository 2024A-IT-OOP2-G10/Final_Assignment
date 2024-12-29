from peewee import Model,CharField, IntegerField, DateField
from .db import db

class Todo(Model): 
    ##Todoリスト実装に必要な情報を管理するデータベース
    ##講義名, Todo名, 締切日
    name = CharField() 
    todo = CharField()
    time = DateField() ##DateFieldで管理してみる

    class Meta:
        database = db
