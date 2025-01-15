from flask import Flask, render_template
from routes import blueprints
from flask_sqlalchemy import SQLAlchemy
from models.db import db

# db
from models import user, todo, lecture, userLectureRelation


app = Flask(__name__)

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

@app.route('/new', methods=['GET', 'POST'])
def new():
    
    # # データ取得
    # users = User.select()
    return render_template('id_new.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # # データ取得
    # users = User.select()
    return render_template('id_login.html')

# @app.route('/home', methods=['GET'])
# def home():
#     return render_template('home.html')

with app.app_context():
    print('open with context')
    db.create_all()  # テーブルを作成

if __name__ == '__main__':
    app.run(port=8888, debug=True)