from peewee import Model,CharField, IntegerField
from .db import db

class MySubject(Model):
    ##自身が追加した講義の情報を取り扱うデータベース
    ##講義名, 欠席回数
    name = CharField()
    rest = IntegerField()

    class Meta:
        database = db
