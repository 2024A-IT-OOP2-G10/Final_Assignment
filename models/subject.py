from peewee import Model,CharField, IntegerField
from .db import db

class Subject(Model):
    ##すべての講義の情報を登録しておくデータベース
    ##講義名, 欠席回数, 曜日, 時間 
    name = CharField()
    absence = IntegerField()
    dayofweek = CharField() ##曜日は数値で管理してみる
    time = IntegerField()

    class Meta:
        database = db
