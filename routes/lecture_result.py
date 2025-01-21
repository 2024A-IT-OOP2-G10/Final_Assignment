from flask import Blueprint, flash, render_template, request, redirect, session, url_for

lectureResult_bp = Blueprint('lecture_result', __name__, url_prefix='/lectures/result')


@lectureResult_bp.route('/')

def index ():
    
    # セッションから保存された講義情報を取得
    local_subjects = session.get('local_subjects', [])
    
    print(local_subjects)
    return render_template('lecture_result.html', local_subjects=local_subjects)