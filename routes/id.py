# Blueprintの作成
from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from models import User

id_bp = Blueprint('id', __name__, url_prefix='/id')

@id_bp.route('')
def index():
    return render_template('id.html')

@id_bp.route('/new', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        user_id = request.form['user']
        password = request.form['pass']
        User.create(user_id=user_id, password=password)

        # Flashメッセージ
        # flash('登録が完了しました！', 'success')

        # 次のページへリダイレクト
        return redirect(url_for('id.success'))

    return render_template('id_new.html')  # 登録ページを表示

@id_bp.route('/success')
def success():
    return render_template('success.html')  # 登録成功ページ

@id_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['user']
        password = request.form['pass']
        
        user = User.get_or_none(User.user_id == user_id)  # Userモデルの検索例
        if user is None:
            print("ユーザーが見つかりません")
            # ユーザーが見つからない場合の処理
            return redirect(url_for('id.index'))  # id Blueprint のトップページにリダイレクト
        
        if user.password == password:  # パスワード一致確認
            # ログイン成功処理
            # session['user_id'] = user_id  # セッションに保存
            print('ログイン成功')
            return redirect(url_for('home.index'))  # ホームページへリダイレクト
        else:
            # ログイン失敗処理
            print('ログイン失敗')
            return redirect(url_for('id.index'))  # id Blueprint のトップページにリダイレクト

    
    # ログインページを表示
    return render_template('id_login.html')

        
    
