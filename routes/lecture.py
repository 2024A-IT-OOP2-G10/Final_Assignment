from flask import Blueprint, render_template, request, redirect, url_for
from models import get_days, get_times, get_classes_by_day_and_time

lecture_bp = Blueprint('main', __name__)
select_classes = []

@lecture_bp.route('/lectures', methods=['GET', 'POST'])


def index():
    
    
    if request.method == 'POST':
        # json形式で受け取る
        data = request.json
        
        res = {
            "status": "success",
        }
        
        if res.get('status') == 'success':
            return redirect(url_for('main.lecture'))
        else:
            return redirect(url_for('main.index'))
    
    lecture_all = [
        {
            "lecture_title": "情報システム演習",
            "weekday": "月曜日",
            "timetable": "1限"
        },
        {
            "lecture_title": "情報システム演習",
            "weekday": "月曜日",
            "timetable": "2限"
        }
    ]
    

    return render_template(
        'lecture.html',
        data = lecture_all,
        
    )

def userLeacture():
    
    if request.method == 'POST':
        # json形式で受け取る
        data = request.json
        
        res = {
            "status": "success",
        }
        
        if res.get('status') == 'success':
            return redirect(url_for('main.lecture'))
        else:
            return redirect(url_for('main.index'))
        
    
    user_lecture = [
        {
            "lecture_id": 1,
            "lecture_title": "情報システム演習",
            "weekday": "月曜日",
            "timetable": "1限",
            "absence_count": 1
        },
        {
            "lecture_id": 2,
            "lecture_title": "情報システム演習",
            "weekday": "月曜日",
            "timetable": "2限",
            "absence_count": 2
        } 
    ]
    
    return redirect(url_for('absence.home', item=user_lecture))