from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    from models.user import User
    from models.todo import Todo
    from models.lecture import Lecture
    from models.userLectureRelation import UserLectureRelation
    
    # テーブル作成
    db.drop_all()  # データベースをリセット
    db.create_all()
    
    # ユーザー
    user1 = User(username='user1', password='password1')
    user2 = User(username='user2', password='password2')
    db.session.add_all([user1, user2])
    
    # コミットしてIDを確定
    db.session.commit()
    
    # 講義
    lecture1 = Lecture(title='情報システム概論', week='月曜日', timetable=1)
    lecture2 = Lecture(title='オブジェクト演習', week='火曜日', timetable=2)
    lecture3 = Lecture(title='データベース論', week='水曜日', timetable=3)
    db.session.add_all([lecture1, lecture2, lecture3])
    db.session.commit()
    
    # リレーション
    userlecture1 = UserLectureRelation(user_id=user1.id, lecture_id=lecture1.id, absence_count=1)
    userlecture2 = UserLectureRelation(user_id=user1.id, lecture_id=lecture2.id, absence_count=2)
    userlecture3 = UserLectureRelation(user_id=user2.id, lecture_id=lecture3.id, absence_count=3)
    db.session.add_all([userlecture1, userlecture2, userlecture3])
    
    # ToDo
    todo1 = Todo(user_id=user1.id, lecture_id=lecture1.id, description='課題1', deadline=datetime(2021, 12, 1))
    todo2 = Todo(user_id=user1.id, lecture_id=lecture2.id, description='課題2', deadline=datetime(2021, 12, 2))
    db.session.add_all([todo1, todo2])
    
    # まとめてコミット
    db.session.commit()
