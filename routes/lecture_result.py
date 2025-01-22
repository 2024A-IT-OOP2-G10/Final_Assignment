from flask import Blueprint, flash, render_template, request, redirect, session, url_for

from models.db import db
from models.lecture import Lecture

lectureResult_bp = Blueprint('lecture_result', __name__, url_prefix='/lectures/result')

@lectureResult_bp.route('/')
def index():
    # セッションから保存された講義情報を取得
    local_subject_ids = session.get('local_subjects', [])
    
    # IDからLectureオブジェクトを再取得
    local_subjects = [Lecture.query.get(subject_id).to_dict() for subject_id in local_subject_ids]

    # 辞書のIDを基にソートする
    sorted_subjects = sorted(local_subjects, key=lambda x: x['id'])

    # 同じ曜日と時限の講義を検出
    for lecture in sorted_subjects:
        lecture['highlight'] = any(
            other['id'] != lecture['id'] and other['week'] == lecture['week'] and other['timetable'] == lecture['timetable']
            for other in sorted_subjects
        )

    return render_template('lecture_result.html', local_subjects=sorted_subjects)
@lectureResult_bp.route('/delete', methods=['POST'])
def delete():
    lecture_id = request.form.get('lecture')  # 削除対象の講義IDを取得
    
    if lecture_id:
        lecture_id = int(lecture_id)  # IDを整数に変換
        local_subject_ids = session.get('local_subjects', [])
        
        # 削除対象を検索
        updated_subjects = [lec_id for lec_id in local_subject_ids if lec_id != lecture_id]
        session['local_subjects'] = updated_subjects  # セッションを更新
    
        return redirect(url_for('lecture_result.index'))
  
    else:
        flash("Invalid subject ID", "error")
        return redirect(url_for('lecture_result.index'))

    
@lectureResult_bp.route('/save', methods=['POST'])
def save():
    # 講義情報を保存する処理（ここではセッション内容をそのまま保持）
    local_subject_ids = session.get('local_subjects', [])
    
    for subject_id in local_subject_ids:
        # DBからLectureオブジェクトを取得
        lecture = Lecture.query.get(subject_id)
        
        if lecture:
            # DBに保存する処理（更新や挿入処理）
            db.session.add(lecture)
            db.session.commit()
    
    return redirect(url_for('home.index'))
