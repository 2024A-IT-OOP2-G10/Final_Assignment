# Blueprintの作成
from flask import Blueprint, render_template, request, url_for, flash, redirect, session
from flask_login import login_user
from models import User
from models.db import db


user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET'])
def get_user():
    if request.method == 'GET':
        user_id = request.args.get('user_id') #クエリパラメータを取得
    user = db.session.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "Userが見つかりません"}
    else: return user
        
        

@user_bp.route('/login', methods=['GET'])
def login():
    # return render_template('id_login.html', ans=ans)
    
    if request.method == 'GET':
        user_id = request.args.get('user')
        password = request.args.get('password')
        
        #user変数で内容に一致する情報があるかをDBと照合する
        #user = User.query.filter_by(username=user_id).first()
        user = db.session.query(User).filter(User.username == user_id).first()
        
        # ユーザーが見つからない場合の処理
        if user is None:
            print("ユーザーが見つかりません")
            pass
          
        elif user.password == password:
            # ans = {"success": "ログインに成功しました"}
            #各ユーザごとのhome.indexがあるのか？\
                
            login_user(user, remember=True)
            
            flash('ログインしました')


            print("success")

            
            
            
            return redirect(url_for('home.index'))# ホームページへリダイレクト
    
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
        
        if not username or not password:
            return redirect(url_for('user.register'))  # フォームへリダイレクト
    
    # データベースの追加処理を行う  
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    ans = {"success": "UserDBの登録に成功しました"}
    flash("ユーザー登録が成功しました！ログインしてください。")
    return redirect(url_for('user.login'))
        
    
