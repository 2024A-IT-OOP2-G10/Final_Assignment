absences = [{
        "absence_id": 1,
        "lecture_title": "情報システム概論",
        "absence_count": 1
    }, {
        "absence_id": 2,
        "lecture_title": "オブジェクト演習",
        "absence_count": 2
    }]

UserData = [
    {"id":1, "username":"name1", "password":"pass1" },
    {"id":2, "username":"name2", "password":"pass2"},
]

todos = [
                    {
                        "todo_id": 1,
                        "lecture_title": "情報システム演習",
                        "description": "課題1の内容",
                        "deadline": "2024-12-10 20:29:57.744098"
                    },
                    {
                        "todo_id": 2,
                        "lecture_title": "オブジェクト演習",
                        "description": "課題2の内容",
                        "deadline": "2024-12-10 20:29:57.744098"
                    }
]

all_lectures_db = [
    {'id': 1, "title": "国語", "week": "月曜日", "timetable": 1},
    {"id": 2, "title": "数学", "week": "火曜日", "timetable": 2},
    {"id": 3, "title": "社会", "week": "火曜日", "timetable": 2},
    {"id": 4, "title": "理科", "week": "木曜日", "timetable": 1},
    {"id": 5, "title": "英語", "week": "金曜日", "timetable": 4}
]

all_user_lectures = [
    {"id": 1, "user_id": 1, "lecture_id": 1, "absence_count": 1},
    {"id": 2, "user_id": 1, "lecture_id": 2, "absence_count": 2},
    # 他のユーザーと講義のデータ
]

all_lectures = [
    {"id": 1, "title": "情報システム概論", "week": "月曜日", "timetable": 1},
    {"id": 2, "title": "オブジェクト演習", "week": "火曜日", "timetable": 2},
    {"id": 3, "title": "データベース論", "week": "水曜日", "timetable": 3},
    # 他の講義データも追加可能
]