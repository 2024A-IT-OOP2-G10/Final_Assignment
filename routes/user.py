# Blueprintの作成
from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from models import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('')
def index():
    return render_template('id.html')

@user_bp.route('/new', methods=['GET'])
def add():
    if request.method == 'POST':
        user_id = request.form['user']
        password = request.form['pass']
        User.create(user_id=user_id, password=password)

        # 次のページへリダイレクト
        return redirect(url_for('id.success'))

    return render_template('id_new.html')  # 登録ページを表示

@user_bp.route('/success')
def success():
    return render_template('success.html')  # 登録成功ページ

@user_bp.route('/login', methods=['GET'])
def login():
    if request.method == 'POST':
        user_id = request.form['user']
        password = request.form['pass']
        
        user = User.get_or_none(User.user_id == user_id)  # Userモデルの検索例
        if user is None:
            # ユーザーが見つからない場合の処理
            print("ユーザーが見つかりません")
            return redirect(url_for('id.index'))
        
        if user.password == password:  # パスワード一致確認
            # ログイン成功処理
            print('ログイン成功')
            return redirect(url_for('home.index'))  # ホームページへリダイレクト
        else:
            # ログイン失敗処理
            print('ログイン失敗')
            return redirect(url_for('id.index'))  # id Blueprint のトップページにリダイレクト

    
    # ログインページを表示
    return render_template('id_login.html')

@user_bp.route('', methods=['GET'])
def user():
    if request.method == 'GET':
        user = {
                "user_id" : 1,
                "name" : "山田太郎"
        }
    return user
        
        

@user_bp.route('/login')
def login():
    # ans1 = {"error": "ログインに失敗しました"}
    # ans2 = {"success": "ログインに成功しました"}
    
    ans = {"success": "ログインに成功しました"}
    return render_template('id_login.html', ans=ans)

@user_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
    
    #データベースの追加処理を行う      
    # "name": "山田太郎",
    # "password": "password"
    
    ans = {"success": "UserDBの登録に成功しました"}
    return render_template('id_new.html', ans=ans)
        
    
