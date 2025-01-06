from flask import Blueprint, Flask, render_template, request, url_for

lecture_bp = Blueprint('lecture', __name__, url_prefix='/lecture')

select_classes = []
# 仮データベース（データベースから持ってくるのはこのリストの形にします）
all_lectures_db = [
    {'id': 1, "class": "国語", "day": "月曜日", "time": 1},
    {"id": 2, "class": "数学", "day": "火曜日", "time": 2},
    {"id": 3, "class": "社会", "day": "火曜日", "time": 2},
    {"id": 4, "class": "理科", "day": "木曜日", "time": 1},
    {"id": 5, "class": "英語", "day": "金曜日", "time": 4}
]

@lecture_bp.route('/list')
def list():
    return render_template('lecture.html', all_lectures_db=all_lectures_db)

# ホームページのルート
@lecture_bp.route('/')
def index():
    sorted_db = sorted(all_lectures_db, key=lambda x: x["id"])
    days = []
    for lecture in sorted_db:
        if lecture["day"] not in days:
            days.append(lecture["day"])
    times = sorted(list({lecture["time"] for lecture in all_lectures_db}))  # 時限もソート
    return render_template('practice.html', days=days, times=times, all_lectures_db=all_lectures_db)

# 曜日・時限の条件に合う講義を返す
@lecture_bp.route('/reference', methods=['POST'])
def reference():
    select_day = request.form.get('day')
    select_time = int(request.form.get('time'))

    # フィルタリングされた講義を取得
    filter_lectures = [
        lecture["class"] for lecture in all_lectures_db
        if lecture["day"] == select_day and lecture["time"] == select_time
    ]

    return render_template(
        'practice.html',
        days=list({lecture["day"] for lecture in all_lectures_db}),
        times=list({lecture["time"] for lecture in all_lectures_db}),
        select_day=select_day,
        select_time=select_time,
        filter_lectures=filter_lectures,
        all_lectures_db=all_lectures_db,
        select_classes=select_classes
    )

# 追加ボタンを押す時に選択した講義を追加
@lecture_bp.route('/select_class', methods=['POST'])
def select_class():
    global select_classes
    select_class = request.form.get('lecture')

    # 追加される講義がまだリストにない場合は追加
    if select_class and select_class not in select_classes:
        select_classes.append(select_class)

    return render_template(
        'practice.html',
        select_classes=select_classes,
        all_lectures_db=all_lectures_db
    )