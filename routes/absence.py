from flask import Blueprint, render_template, request, redirect, url_for
from models import MySubject

# Blueprintの作成
product_bp = Blueprint('absence', __name__, url_prefix='/absence')

@product_bp.route('/')
def home():
    absences = MySubject.select()
    return render_template('home.html', item=absences)

@product_bp.route('/result', methods=['GET', 'POST'])
def result():
    
    # POSTで送られてきたデータを変更
    if request.method == 'POST':
        name = request.form['name']
        absence = request.form['absence']
        query = MySubject.update(absence=absence).where(MySubject.name == name)
        query.execute()
        return redirect(url_for('home'))
    
    return render_template('absence.html')