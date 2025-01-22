from flask import Blueprint, render_template, request, redirect, url_for, session
from models import  UserLectureRelation, Lecture, User
from models import data
from models.db import db

# Blueprintの作成
absence_bp = Blueprint('absence', __name__, url_prefix='/absence')

# all_user_lectures = [
#     {"id": 1, "user_id": 1, "lecture_id": 1, "absenceCount": 1},
#     {"id": 2, "user_id": 1, "lecture_id": 2, "absenceCount": 2},
#     # 他のユーザーと講義のデータ
# ]

# mylecture = [
#                 { "id":1,"title": "情報システム概論", "week": "月曜日", },
#                 { "id":2,"title": "オブジェクト演習", "week": "火曜日",}
#                 ]

# all_lectures = [
#     {"id": 1, "title": "情報システム概論", "week": "月曜日", "timetable": 1},
#     {"id": 2, "title": "オブジェクト演習", "week": "火曜日", "timetable": 2},
#     {"id": 3, "title": "データベース論", "week": "水曜日", "timetable": 3},
#     # 他の講義データも追加可能
# ]


@absence_bp.route('/result', methods=['GET', 'POST'])
def result():
    
    user_id = session.get('user_id')
    
    
    if request.method == 'POST':
        absence_count = request.form.get('absence')
        lecture = request.form.get('lecture')
        print(absence_count)
        print(lecture)

        # user_lecture_relation を取得
        user_lecture_relation = UserLectureRelation.query.filter_by(
        user_id=user_id, lecture_id= int(lecture)).first()

        # user_lecture_relation が None でないことを確認
        if user_lecture_relation:
            user_lecture_relation.absence_count = absence_count
            db.session.commit()
        else:
            user_lecture_relation = UserLectureRelation(
                user_id=user_id,
                lecture_id=lecture_id,
                absence_count=absence_count
            )
            db.session.add(user_lecture_relation)
            db.session.commit()
            
        return redirect(url_for('home.index'))
            
    elif request.method == 'GET':
        
        lecture_id = request.args.get('lecture')
        print(lecture_id)
        
        selected_lecture = db.session.query(
            Lecture.id, Lecture.title, UserLectureRelation.absence_count
        ).join(UserLectureRelation, Lecture.id == UserLectureRelation.lecture_id) \
        .filter(UserLectureRelation.user_id == user_id, Lecture.id == lecture_id).first()
        print(selected_lecture)
        return render_template('absence_result.html', lecture=selected_lecture)


    # if request.method == 'POST':
    #     name = request.form['name']
    #     absence = request.form['absence']
    #     # query = MySubject.update(absence=absence).where(MySubject.name == name)
    #     # query.execute()
    #     return redirect(url_for('absence.result'))


@absence_bp.route('/', methods=['GET'])

def index():
    
    # 本来はDBから講義データを取得する
    mylectureData = get_absences(session.get('user_id'))
    
    return render_template('absence.html', lectures=mylectureData)
  
@absence_bp.route('/absences', methods=['GET'])  
def absences():
    
    if request.method == 'GET':
        week = request.args.get('weekday')
        
        user_id = session.get('user_id')
        
        # DBからuserとweekが一致する講義データを取得する
        mylectureData = db.session.query(
            Lecture.id, Lecture.title, Lecture.week
        ).join(UserLectureRelation, Lecture.id == UserLectureRelation.lecture_id) \
        .filter(UserLectureRelation.user_id == user_id, Lecture.week == week).all()
        
        
        
        return render_template('absence.html', subjects= mylectureData, day=week)       
        
        
        
def get_absences(user_id):
    
    print(db)
    
    #SQLAlchemy用
    
    absences = db.session.query(
        UserLectureRelation.id, Lecture.title, UserLectureRelation.absence_count,UserLectureRelation.lecture_id
    ).join(Lecture, Lecture.id == UserLectureRelation.lecture_id) \
    .filter(UserLectureRelation.user_id == user_id).all()
            
    
    # 仮データ
    # absences = [{
    #     "absence_id": 1,
    #     "lecture_title": "情報システム概論",
    #     "absence_count": 1
    # }, {
    #     "absence_id": 2,
    #     "lecture_title": "オブジェクト演習",
    #     "absence_count": 2
    # }]
    
    
    
    return absences