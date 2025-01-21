# Blueprintの作成
from flask import Blueprint, render_template, session, redirect, url_for
from .absence import get_absences

home_bp = Blueprint('home', __name__, url_prefix='/home')

@home_bp.route('/')
def index():
    
    # セッションからusernameを取得
    username = session.get('username')

    # usernameがセッションに保存されていない場合、ログインページにリダイレクトすることもできます
    if username:
        # ユーザーに対応する欠席情報を取得（例：ユーザーごとに欠席情報があると仮定）
        absences = get_absences(username)
    else:
        absences = []
    
    return render_template('home.html', absences=absences)