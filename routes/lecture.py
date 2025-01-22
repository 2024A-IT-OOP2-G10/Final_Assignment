from flask import Blueprint, flash, render_template, request, redirect, session, url_for
from flask_login import login_required
from models.db import db
from models.lecture import Lecture
from models.userLectureRelation import UserLectureRelation

lecture_bp = Blueprint('lectures', __name__, url_prefix='/lectures')

# 特定の曜日・時限に対応する講義を返す
def get_classes_by_day_and_time(day, time):
    return Lecture.query.filter_by(week=day, timetable=time).all()

@lecture_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    day = request.args.get('day')
    time = request.args.get('time')
    
    classes = []
    if day and time:
        try:
            time = int(time)  # 時限は整数に変換
            classes = get_classes_by_day_and_time(day, time)
        except ValueError:
            pass  # 時限が整数でない場合は無視

    # セッションに保存された選択された講義を取得
    local_subject_ids = session.get('local_subjects', [])
    local_subjects = [Lecture.query.filter_by(id=subject_id).first().to_dict() for subject_id in local_subject_ids]

    return render_template(
        'lecture.html',
        selected_day=day,
        selected_time=time,
        classes=[lecture.to_dict() for lecture in classes],
        local_subjects=local_subjects,
    )

@lecture_bp.route('/add', methods=['POST'])
@login_required
def add():
    try:
        subject_id = int(request.form.get('lecture'))  # lecture_idを取得
    except (TypeError, ValueError):
        flash("無効な講義IDです", "error")
        return redirect(url_for('lectures.index'))

    # 対応する講義を取得
    subject = Lecture.query.filter_by(id=subject_id).first()

    if subject:
        
        myLecture = db.session.query(
            UserLectureRelation.lecture_id,
            UserLectureRelation.user_id
        ).filter(UserLectureRelation.lecture_id == subject_id).first()
        
        if myLecture:
            flash("すでに登録されている講義です", "error")
            return redirect(url_for('lectures.index'))
        
        # セッションに講義IDを追加
        
        localsubject_ids = session.get('local_subjects', [])
        
        if subject_id not in localsubject_ids:
            
            localsubject_ids.append(subject_id)
            session['local_subjects'] = localsubject_ids
        
        
        

    else:
        flash("講義が見つかりません", "error")
        
    return redirect(url_for('lectures.index'))



@lecture_bp.route('/select_class', methods=['POST'])
@login_required
def select_class():
    lecture_id = request.form.get('lecture')
    
    if lecture_id:
        # ID を元に該当する講義を取得
        lecture = Lecture.query.filter_by(id=lecture_id).first()
        
        if lecture:
            # セッションに講義IDを追加
            local_subject_ids = session.get('local_subjects', [])
            if lecture.id not in local_subject_ids:
                local_subject_ids.append(lecture.id)
                session['local_subjects'] = local_subject_ids
                
        else:
            flash("講義が見つかりません", "error")
    
    return redirect(url_for('lecture_result.index'))
