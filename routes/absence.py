from flask import Blueprint, render_template, request, redirect, url_for
from models import MySubject

# Blueprintの作成
absence_bp = Blueprint('absence', __name__, url_prefix='/absence')

@absence_bp.route('/')
def home():
    absences = MySubject.select()
    return render_template('home.html', item=absences)

@absence_bp.route('/result', methods=['GET', 'POST'])
def result():
    
    # POSTで送られてきたデータを変更
    if request.method == 'POST':
        name = request.form['name']
        absence = request.form['absence']
        query = MySubject.update(absence=absence).where(MySubject.name == name)
        query.execute()
        return redirect(url_for('home'))
    
    return render_template('absence.html')


@absence_bp.route('', methods=['GET','POST'])
def absences():
    if request.method == 'GET':
            absences = [
                        {
                        "absence_id": 1,
                        "lecture_title": "情報システム概論",
                        "absence_count": 1
                        },
                        {
                        "absence_id": 2,
                        "lecture_title": "オブジェクト演習",
                        "absence_count": 2  
                        }
                    ]
            return render_template('absence_result.html', absences=absences)
    elif request.method == 'POST':
            user_id = request.form['user_id']
            lecture_title = request.form['lecture_title']
            absence_count = request.form['absence_count']
            #この情報をデータベースに登録
            ans = {"success": "DBへの登録を完了しました"}
            return render_template('absence_result.html', ans=ans)
        
        
        
    