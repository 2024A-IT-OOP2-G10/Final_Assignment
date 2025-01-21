from flask import Blueprint, flash, render_template, request, redirect, session, url_for

lecture_bp = Blueprint('lectures', __name__, url_prefix='/lectures')

# 仮データベースとして活用（この形にする）
all_lectures_db = [
    {'id': 1, "class": "国語", "day": "月曜日", "time": 1},
    {"id": 2, "class": "数学", "day": "火曜日", "time": 2},
    {"id": 3, "class": "社会", "day": "火曜日", "time": 2},
    {"id": 4, "class": "理科", "day": "木曜日", "time": 1},
    {"id": 5, "class": "英語", "day": "金曜日", "time": 4}
]

# 特定の曜日・時限に対応する講義を返す
def get_classes_by_day_and_time(day, time):
    return [lecture for lecture in all_lectures_db if lecture["day"] == day and lecture["time"] == time]

@lecture_bp.route('/', methods=['GET', 'POST'])
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
    local_subjects = session.get('local_subjects', [])
    
    return render_template(
        'lecture.html',
        selected_day=day,
        selected_time=time,
        classes=classes,
        local_subjects=local_subjects,  # sessionから取得したlocal_subjectsを渡す
    )

@lecture_bp.route('/add', methods=['POST'])
def add():
    
    print("add")
    try:
        subject_id = int(request.form.get('lecture'))  # lecture_idを取得
        
        print(subject_id)
    
        
    # IDが整数でない場合の例外処理
    except (TypeError, ValueError):
        flash("Invalid subject ID", "error")
        return redirect(url_for('lectures.index'))
    
    # 仮データidに対応する講義を取得
    subject = next((lecture for lecture in all_lectures_db if lecture["id"] == subject_id), None)
    
    if subject:
        # セッションに講義を追加
        local_subjects = session.get('local_subjects', [])
        if subject not in local_subjects:
            local_subjects.append(subject)
            session['local_subjects'] = local_subjects
            
        print(local_subjects)
    else:
        flash("Subject not found", "error")
        
    return redirect(url_for('lectures.index'))

@lecture_bp.route('/select_class', methods=['POST'])
def select_class():
    lecture_id = request.form.get('lecture')
    
    if lecture_id:
        # ID を元に該当する講義を取得
        lecture = next((lec for lec in all_lectures_db if str(lec["id"]) == lecture_id), None)
        if lecture:
            # セッションに選ばれた講義を追加
            local_subjects = session.get('local_subjects', [])
            if lecture not in local_subjects:
                local_subjects.append(lecture)
                session['local_subjects'] = local_subjects

    return redirect(url_for('lecture_result.index'))
