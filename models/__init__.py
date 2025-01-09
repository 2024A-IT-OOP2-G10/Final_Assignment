from .db import db
from .subject import Subject
from .my_subject import MySubject
from .todo import Todo
from .lecture import get_days, get_times, get_classes_by_day_and_time


#モデルのリストを定義
MODELS = [
    Subject,
    MySubject,
    Todo
]

def initialize_database():
    db.connect()
    db.create_tables(MODELS, safe=True)
    db.close()
    
##Todo Subjectデータベースへの情報追加