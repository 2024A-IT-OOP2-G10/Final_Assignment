from .db import db
from .subject import Subject
from .my_subject import MySubject
from .todo import Todo


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