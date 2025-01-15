from flask import Blueprint, render_template, request, redirect, url_for



lecture_bp = Blueprint('main', __name__)
select_classes = []

# 仮データベースとして活用（この形にする）
all_lectures_db = [
    {'id': 1, "class": "国語", "day": "月曜日", "time": 1},
    {"id": 2, "class": "数学", "day": "火曜日", "time": 2},
    {"id": 3, "class": "社会", "day": "火曜日", "time": 2},
    {"id": 4, "class": "理科", "day": "木曜日", "time": 1},
    {"id": 5, "class": "英語", "day": "金曜日", "time": 4}
]

@lecture_bp.route('/', methods=['GET', 'POST'])

# 曜日を返す
def get_days():
    return list(set([lecture["day"] for lecture in all_lectures_db]))

# 時限を返す
def get_times():
    return list(set([lecture["time"] for lecture in all_lectures_db]))

# 特定の曜日・時限に対応する講義を返す
def get_classes_by_day_and_time(day, time):
    return [lecture for lecture in all_lectures_db if lecture["day"] == day and lecture["time"] == time]

    
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
