from flask import Blueprint, flash, render_template, request, redirect, session, url_for

lectureResult_bp = Blueprint('lecture_result', __name__, url_prefix='/lectures/result')


@lectureResult_bp.route('/')
def index():
    # セッションから保存された講義情報を取得
    local_subjects = session.get('local_subjects', [])
    sorted_subjects = sorted(local_subjects, key=lambda x: x['id'])

    # 同じ曜日と時限の講義を検出
    for lecture in sorted_subjects:
        lecture['highlight'] = any(
            other['id'] != lecture['id'] and other['day'] == lecture['day'] and other['time'] == lecture['time']
            for other in sorted_subjects
        )

    return render_template('lecture_result.html', local_subjects=sorted_subjects)

@lectureResult_bp.route('/delete', methods=['POST'])
def delete():
    lecture_id = request.form.get('lecture')  # 削除対象の講義IDを取得
    
    if lecture_id:
            lecture_id = int(lecture_id)  # IDを整数に変換
            local_subjects = session.get('local_subjects', [])
            
            # 削除対象を検索
            updated_subjects = [lec for lec in local_subjects if lec["id"] != lecture_id]
            session['local_subjects'] = updated_subjects  # セッションを更新
    
    return redirect(url_for('lecture_result.index'))

@lectureResult_bp.route('/save', methods=['POST'])
def save():
    # 講義情報を保存する処理（ここではセッション内容をそのまま保持）
    local_subjects = session.get('local_subjects', [])
    
    return redirect(url_for('home'))