from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, UserLectureRelation, Lecture, User
from models import data

# Blueprintの作成
absence_bp = Blueprint('absence', __name__, url_prefix='/absence')

all_user_lectures = [
    {"id": 1, "user_id": 1, "lecture_id": 1, "absenceCount": 1},
    {"id": 2, "user_id": 1, "lecture_id": 2, "absenceCount": 2},
    # 他のユーザーと講義のデータ
]

all_lectures = [
    {"id": 1, "title": "情報システム概論", "week": "月曜日", "timetable": 1},
    {"id": 2, "title": "オブジェクト演習", "week": "火曜日", "timetable": 2},
    {"id": 3, "title": "データベース論", "week": "水曜日", "timetable": 3},
    # 他の講義データも追加可能
]


@absence_bp.route('/result', methods=['GET', 'POST'])
def result():
    
    user_id = session.get('user_id')
    lecture_id = request.args.get('name')
    print(lecture_id)
    
    selected_lecture = next((lecture for lecture in data.all_lectures_db if lecture['id'] == lecture_id), None)
    print(selected_lecture)

    
    # if not lecture_id:
    #     return redirect(url_for('absences'))
    
    if request.method == 'POST':
        absence_count = request.form.get('absence')
        
        #user_id, lecture_id, absence_count情報からDBを変更する
        # userlecturerelation = UserLectureRelation.query.filter_by(user_id=user_id, lecture_id=lecture_id).first()
        # userlecturerelation.absence_count = absence_count
        # db.session.commit()
        
        
        return render_template('absence.html')
    
    
    return render_template('absence_result.html', lecture=selected_lecture)

    # if request.method == 'POST':
    #     name = request.form['name']
    #     absence = request.form['absence']
    #     # query = MySubject.update(absence=absence).where(MySubject.name == name)
    #     # query.execute()
    #     return redirect(url_for('absence.result'))


@absence_bp.route('/', methods=['GET'])
def absences():
    
    #SQLAlchemy用
    # user_id = session.get('user_id')
    # subjects = db.session.query(
    #         Lecture.id, Lecture.title, Lecture.week
    #     ).join(UserLectureRelation, Lecture.id == UserLectureRelation.lecture_id) \
    #     .filter(UserLectureRelation.user_id == user_id) \
    #     .all()
    
    if request.method == 'GET':
        mylecture = [{ "id":1,"title": "情報システム概論", "week": "月曜日", },
                     { "id":2,"title": "オブジェクト演習", "week": "火曜日",}]
        day = request.args.get('weekday')
        subjects = [lecture for lecture in mylecture if lecture['week'] == day]
        return render_template('absence.html', subjects=subjects, day=day)       
        
        
        
def get_absences(user_id):
    
    #SQLAlchemy用
    # absences = db.session.query(
    #         UserLectureRelation.user_id,
    #         Lecture.title,
    #         UserLectureRelation.absence_count
    #     ).join(Lecture, UserLectureRelation.lecture_id == Lecture.id) \
    #     .filter(UserLectureRelation.user_id == user_id) \
    #     .all()
            
    
    # 仮データ
    absences = [{
        "absence_id": 1,
        "lecture_title": "情報システム概論",
        "absence_count": 1
    }, {
        "absence_id": 2,
        "lecture_title": "オブジェクト演習",
        "absence_count": 2
    }]
    
    return absences