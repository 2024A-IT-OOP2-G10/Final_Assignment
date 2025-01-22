from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# テーブル作成
# テーブルが存在する場合は初期化をしない
def init_db():
    from models.user import User
    from models.todo import Todo
    from models.lecture import Lecture
    from models.userLectureRelation import UserLectureRelation

    db.create_all()
    
    # データが存在する場合は初期化しない
    if User.query.first() or Lecture.query.first() or Todo.query.first() or UserLectureRelation.query.first():
        print("データベースはすでにデータがあります")
        return

    print("データベースを初期化します...")
    
    # ユーザー
    user1 = User(username='user1', password='password1')
    user2 = User(username='user2', password='password2')
    
    # 講義
    lectures = [
        Lecture(title='情報システム概論', week='月曜日', timetable=1),
        Lecture(title='オブジェクト演習', week='火曜日', timetable=2),
        Lecture(title='データベース論', week='水曜日', timetable=3),
        Lecture(title='アルゴリズム入門', week='月曜日', timetable=1),
        Lecture(title='ネットワーク基礎', week='月曜日', timetable=2),
        Lecture(title='コンピュータ構造', week='火曜日', timetable=3),
        Lecture(title='情報セキュリティ', week='火曜日', timetable=4),
        Lecture(title='プログラミング基礎', week='水曜日', timetable=1),
        Lecture(title='ソフトウェア設計', week='水曜日', timetable=2),
        Lecture(title='人工知能基礎', week='木曜日', timetable=3),
        Lecture(title='機械学習概論', week='木曜日', timetable=4),
        Lecture(title='データサイエンス', week='金曜日', timetable=1),
        Lecture(title='統計学入門', week='金曜日', timetable=2),
        Lecture(title='クラウドコンピューティング', week='月曜日', timetable=3),
        Lecture(title='オペレーティングシステム', week='火曜日', timetable=4),
        Lecture(title='プログラミング応用', week='水曜日', timetable=3),
        Lecture(title='データベース設計', week='木曜日', timetable=1),
        Lecture(title='ソフトウェア工学', week='木曜日', timetable=2),
        Lecture(title='情報検索技術', week='金曜日', timetable=3),
        Lecture(title='ヒューマンインターフェース', week='金曜日', timetable=4),
        Lecture(title='モバイルアプリ開発', week='月曜日', timetable=4),
        Lecture(title='自然言語処理', week='火曜日', timetable=1),
        Lecture(title='分散システム', week='火曜日', timetable=2),
    ]

    
    # リレーション
    userlecture1 = UserLectureRelation(user_id=user1.id, lecture_id=lectures[0].id, absence_count=1)
    userlecture2 = UserLectureRelation(user_id=user1.id, lecture_id=lectures[1].id, absence_count=2)
    userlecture3 = UserLectureRelation(user_id=user2.id, lecture_id=lectures[2].id, absence_count=3)
    
    # ToDo
    Todo1=Todo(user_id=user1.id, lecture_id=lectures[0].id, description='課題1', deadline=datetime(2021, 12, 1))
    # todo1 = Todo(user_id=user1.id, lecture_id=lectures[0].id, description='課題1', deadline=datetime(2021, 12, 1))
    # todo2 = Todo(user_id=user1.id, lecture_id=lectures[1].id, description='課題2', deadline=datetime(2021, 12, 2))
    
    # データベースへ保存
    
    # ユーザーを保存し、IDを確定
    db.session.add_all([user1, user2])
    db.session.commit()

    # 講義を保存し、IDを確定
    db.session.add_all(lectures)
    db.session.commit()
    
    db.session.add_all([user1, user2, userlecture1, userlecture2, userlecture3, Todo1])
    db.session.commit()
