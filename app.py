from flask import Flask, render_template
import flask_login
from flask_login import UserMixin
from models.db import db
from models.user import User
from routes import blueprints

app = Flask(__name__)

# セッション管理用に secret_key を設定
app.secret_key = 'your-unique-secret-key' 
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# データベースの初期化
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sample_flask.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    return render_template('id.html')


@login_manager.user_loader
def load_user(user_id):
    
    return User(user_id)
    

@app.route('/user', methods=['GET', 'POST'])
def new():
    
    # # データ取得
    # users = User.select()
    return render_template('id_new.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
    
#     # # データ取得
#     # users = User.select()
#     return render_template('id_login.html')

with app.app_context():
    print('open with context')
    db.create_all()  # テーブルを作成

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8888, debug=True)