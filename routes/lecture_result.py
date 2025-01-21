from flask import Blueprint, flash, render_template, request, redirect, session, url_for

lectureResult_bp = Blueprint('lecture_result', __name__, url_prefix='/lectures/result')


@lectureResult_bp.route('/')

def index ():
    
    # セッションから保存された講義情報を取得
    local_subjects = session.get('local_subjects', [])
    
    print(local_subjects)
    return render_template('lecture_result.html', local_subjects=local_subjects)

@lectureResult_bp.route('/add', methods=['POST'])
# 保存
def add():
    
    # セッションから保存された講義情報を取得
    local_subjects = session.get('local_subjects', [])
    
    # 本来はlocal_subjectsをDBに保存する処理が必要
    
    # セッションに講義を初期化
    session['local_subjects'] = []
    
    return redirect(url_for('home.index'))