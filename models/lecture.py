# 仮データベースとして活用（この形にする）
all_lectures_db = [
    {'id': 1, "class": "国語", "day": "月曜日", "time": 1},
    {"id": 2, "class": "数学", "day": "火曜日", "time": 2},
    {"id": 3, "class": "社会", "day": "火曜日", "time": 2},
    {"id": 4, "class": "理科", "day": "木曜日", "time": 1},
    {"id": 5, "class": "英語", "day": "金曜日", "time": 4}
]

# 曜日を返す
def get_days():
    return list(set([lecture["day"] for lecture in all_lectures_db]))

# 時限を返す
def get_times():
    return list(set([lecture["time"] for lecture in all_lectures_db]))

# 特定の曜日・時限に対応する講義を返す
def get_classes_by_day_and_time(day, time):
    return [lecture for lecture in all_lectures_db if lecture["day"] == day and lecture["time"] == time]
