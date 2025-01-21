from flask import Blueprint, render_template, request, redirect, url_for, session
from models import db, UserLectureRelation, Lecture, User

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
    # POSTで送られてきたデータを変更
    if request.method == 'POST':
        name = request.form['name']
        absence = request.form['absence']
        # query = MySubject.update(absence=absence).where(MySubject.name == name)
        # query.execute()
        return redirect(url_for('home'))
    
    return render_template('absence.html')


@absence_bp.route('', methods=['GET','POST'])
def absences():
    user_id = session.get('user_id')
    day = ""
    # absences = db.session.query(
    #         UserLectureRelation.user_id,
    #         Lecture.title,
    #         Lecture.week,
    #         UserLectureRelation.absence_count
    #     ).join(Lecture, UserLectureRelation.lecture_id == Lecture.id) \
    #     .filter(UserLectureRelation.user_id == user_id) \
    #     .all()
    if request.method == 'GET':
        
        mylecture = [{"user_id": 1, "title": "情報システム概論", "week": "月曜日", "absence_count": 2},
        {"user_id": 1, "title": "オブジェクト演習", "week": "火曜日", "absence_count": 1}]
        day = request.args.get('weekday')
        subjects = [lecture for lecture in mylecture if lecture['week'] == day]
        return render_template('absence.html', subjects=subjects, day=day)
    elif request.method == 'POST':
            

    # 曜日が選択されていれば、その曜日に関連する講義をフィルタリング
            
            #queryパラメータで取得する場合
            #user_id = request.args.get('user_id')
            #lecture_title = request.args.get('lecture_title')
            #absence_count = request.args.get('absence_Count')
            
            #この情報をデータベースに登録
            
            # new_absence = UserLectureRelation(user_id=user_id, lecture_title=lecture_title, absenceCount=absence_count)
            # db.session.add(new_absence)
            # db.session.commit()
            
            return render_template('absence.html', absences=absences, day=day, subject=subjects)
        
        
        
def get_absences(user_id):
    # absences = MySubject.select()
    # UserLectures = UserLectureRelation.query.filter_by(id=user_id).all()
    # UserLectures = [ul for ul in all_user_lectures if ul['user_id'] == user_id]
    # absences = []
    # for UserLecture in UserLectures:
    #     #lecture_titleを取得
    #     # lecture = Lecture.query.filter_by(id=UserLecture.lecture_id).first()
    #     lecture = next((l for l in all_lectures if l['id'] == ['lecture_id']), None)
    #     if not lecture:
    #         continue
            
    #     absences.append({
    #         "absence_id" : UserLecture.id,
    #         "lecture_title" : lecture.title,
    #         "absence_count" : UserLecture.absence_count
    #     })
            
    
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