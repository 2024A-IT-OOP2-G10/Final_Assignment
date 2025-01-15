# Blueprintの作成
from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from models import User
from models import db


user_bp = Blueprint('user', __name__, url_prefix='/user')

# @user_bp.route('')
# def index():
#     return render_template('id.html')

# @user_bp.route('/new', methods=['GET'])
# def add():
#     if request.method == 'POST':
#         user_id = request.form['user']
#         password = request.form['pass']
#         User.create(user_id=user_id, password=password)

#         # 次のページへリダイレクト
#         return redirect(url_for('id.success'))

#     return render_template('id_new.html')  # 登録ページを表示

# @user_bp.route('/success')
# def success():
#     return render_template('success.html')  # 登録成功ページ

# @user_bp.route('/login', methods=['GET'])
# def login():
#     if request.method == 'POST':
#         user_id = request.form['user']
#         password = request.form['pass']
        
#         user = User.get_or_none(User.user_id == user_id)  # Userモデルの検索例
#         if user is None:
#             # ユーザーが見つからない場合の処理
#             print("ユーザーが見つかりません")
#             return redirect(url_for('id.index'))
        
#         if user.password == password:  # パスワード一致確認
#             # ログイン成功処理
#             print('ログイン成功')
#             return redirect(url_for('home.index'))  # ホームページへリダイレクト
#         else:
#             # ログイン失敗処理
#             print('ログイン失敗')
#             return redirect(url_for('id.index'))  # id Blueprint のトップページにリダイレクト

    
#     # ログインページを表示
#     return render_template('id_login.html')

@user_bp.route('', methods=['GET'])
def get_user():
    if request.method == 'GET':
        user_id = request.args.get('user_id') #クエリパラメータを取得
        user = User.query.filter_by(username=user_id).first() #DBと照合
    if not user:
        return {"error": "Userが見つかりません"}
    else: return user
        
        

@user_bp.route('/login')
def login():
    # ans1 = {"error": "ログインに失敗しました"}
    # ans2 = {"success": "ログインに成功しました"}
    
    
    ans = {"success": "ログインに成功しました"}
    # return render_template('id_login.html', ans=ans)
    if request.method == 'POST':
        user_id = request.form['name']
        password = request.form['password']
        
        #queryパラメータで取得する場合
        #user_id = request.args.get('name')
        #password = request.args.get('password')
        
        #user変数で内容に一致する情報があるかをDBと照合する
        user = User.query.filter_by(username=user_id).first()
        
    if user is None:
        # ユーザーが見つからない場合の処理
        ans = {"error": "ログインに失敗しました"}
    elif user.password == password:  # パスワード一致確認
        ans = {"success": "ログインに成功しました"}
        #各ユーザごとのhome.indexがあるのか？
        return redirect(url_for('home.index'))  # ホームページへリダイレクト
    else:
        # ログイン失敗処理
        ans = {"error": "ログインに失敗しました"}
        return render_template('id.html', ans=ans)
        
@user_bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        
        #queryパラメータで取得する場合
        #name = request.args.get('name')
        #password = request.args.get('password')
    
    #データベースの追加処理を行う  
    new_user = User(username=name, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    ans = {"success": "UserDBの登録に成功しました"}
    return render_template('id_new.html', ans=ans)
        
    
