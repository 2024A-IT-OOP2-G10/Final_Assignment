# Blueprintの作成
from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from models import User
from models import db

UserData = [
    {"id":1, "username":"name1", "password":"pass1" },
    {"id":2, "username":"name2", "password":"pass2"},
]


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('', methods=['GET'])
def get_user():
    if request.method == 'GET':
        user_id = request.args.get('user_id') #クエリパラメータを取得
        #user = User.query.filter_by(username=user_id).first() #DBと照合
    user = next((user for user in UserData if user['username'] == user_id), None)
    
    if not user:
        return {"error": "Userが見つかりません"}
    else: return user
        
        

@user_bp.route('/login', methods=['GET'])
def login():
    # ans1 = {"error": "ログインに失敗しました"}
    # ans2 = {"success": "ログインに成功しました"}
    # return render_template('id_login.html', ans=ans)
    
    if request.method == 'GET':
        user_id = request.args.get('user')
        password = request.args.get('password')
        
        #user変数で内容に一致する情報があるかをDBと照合する
        #user = User.query.filter_by(username=user_id).first()
        user = next((user for user in UserData if user['username'] == user_id), None)
        
        if user is None:
            pass
            # ユーザーが見つからない場合の処理
        elif user['password'] == password:  # パスワード一致確認
            # ans = {"success": "ログインに成功しました"}
            #各ユーザごとのhome.indexがあるのか？
            session['username'] = request.args.get('user')
            return redirect(url_for('home.index'))# ホームページへリダイレクト
    
    # POSTリクエストの場合、ログインフォームを表示
    return render_template('id_login.html')
        
@user_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        # GETリクエストで登録フォームを表示
        return render_template('id_new.html')
    
    if request.method == 'POST':
        # フォームから送信されたデータを取得
        username = request.form.get('user')
        password = request.form.get('password')
        
        # バリデーション（例: 空チェック）
        if not username or not password:
            return redirect(url_for('user.register'))  # フォームへリダイレクト
        
        #queryパラメータで取得する場合
        #name = request.args.get('name')
        #password = request.args.get('password')
    
    #データベースの追加処理を行う  
    # new_user = User(username=username, password=password)
    # db.session.add(new_user)
    # db.session.commit()
    
    ans = {"success": "UserDBの登録に成功しました"}
    flash("ユーザー登録が成功しました！ログインしてください。")
    return redirect(url_for('user.login'))  # ログインページへリダイレクト
    #return render_template('success.html', ans=ans)
        
    
