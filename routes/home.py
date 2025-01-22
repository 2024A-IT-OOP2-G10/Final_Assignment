# Blueprintの作成
from flask import Blueprint, render_template, session, redirect, url_for # type: ignore
from flask_login import login_required,current_user # type: ignore

from routes.todo import get_todo
from .absence import get_absences

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
@login_required
def index():
    
    # セッションからusernameを取得
    username = current_user.get_id()
    print(username)

    # usernameがセッションに保存されていない場合、ログインページにリダイレクトすることもできます
    if username:
        # ユーザーに対応する欠席情報を取得（例：ユーザーごとに欠席情報があると仮定）
        absences = get_absences(username)
        
        # dbからtodoListを取得するapiを呼び出す
        
        todoList = get_todo(username)
    else:
        absences = []
        todoList = []
    
    return render_template('home.html', absences=absences,todoList=todoList)    