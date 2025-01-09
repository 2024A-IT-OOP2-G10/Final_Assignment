from flask import Blueprint, render_template, request, redirect, url_for
from models import get_days, get_times, get_classes_by_day_and_time

lecture_bp = Blueprint('main', __name__,url_prefix='/lecture')
select_classes = []

@lecture_bp.route('/lecture', methods=['GET', 'POST'])
def index():
    global select_classes
    days = get_days()
    times = get_times()
    selected_day = request.form.get('day')
    selected_time = request.form.get('time')
    classes = []

    if selected_day and selected_time:
        classes = get_classes_by_day_and_time(selected_day, int(selected_time))

    return render_template(
        'lecture.html',
        days=days,
        times=times,
        selected_day=selected_day,
        selected_time=selected_time,
        classes=classes,
        select_classes=select_classes
    )


@lecture_bp.route('/select_class', methods=['POST'])
def select_class():
    global select_classes
    select_class = request.form.get('lecture')

    if select_class and select_class not in select_classes:
        select_classes.append(select_class)

    return redirect(url_for('main.index'))  # フォームをリダイレクトしてリスト更新
