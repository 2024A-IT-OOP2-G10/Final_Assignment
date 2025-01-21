from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from models import User
from models import Subject
from models import MySubject

subject_bp = Blueprint('subject', __name__, url_prefix='/subject')

# 仮データ
all_lectures_db = [
    {'id': 1, "class": "国語", "day": "月曜日", "time": 1},
    {"id": 2, "class": "数学", "day": "火曜日", "time": 2},
    {"id": 3, "class": "社会", "day": "火曜日", "time": 2},
    {"id": 4, "class": "理科", "day": "木曜日", "time": 1},
    {"id": 5, "class": "英語", "day": "金曜日", "time": 4}
]

@subject_bp.route('/')
def index():
    # セッションから保存された講義情報を取得
    local_subjects = session.get('local_subjects', [])
    return render_template('lecture.html', local_subjects=local_subjects)


@subject_bp.route('/add', methods=['POST'])
def add():
    try:
        subject_id = int(request.form.get('lecture_id'))  # lecture_idを取得
    except (TypeError, ValueError):
        flash("Invalid subject ID", "error")
        return redirect(url_for('subject.index'))

    # 仮データidに対応する講義を取得
    subject = next((lecture for lecture in all_lectures_db if lecture["id"] == subject_id), None)
    
    if subject:
        # セッションに講義を追加
        local_subjects = session.get('local_subjects', [])
        if subject not in local_subjects:
            local_subjects.append(subject)
            session['local_subjects'] = local_subjects  # 更新された講義をセッションに保存
    else:
        flash("Subject not found", "error")

    return redirect(url_for('subject.index'))
