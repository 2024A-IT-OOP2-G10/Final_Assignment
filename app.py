from flask import Flask, render_template
from models import initialize_database
from routes import blueprints

app = Flask(__name__)

# データベースの初期化
initialize_database()

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

if __name__ == '__main__':
    app.run(port=8888, debug=True)