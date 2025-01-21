from flask import Flask, render_template
from routes import blueprints

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# セッション管理用に secret_key を設定
app.secret_key = 'your-unique-secret-key'  # 安全でランダムなキーを設定

# データベースの初期化

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)

# ホームページのルート
@app.route('/')
def index():
    return render_template('id.html')

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
    
    
# セッション管理用に secret_key を設定
app.secret_key = 'your-unique-secret-key'  # 安全でランダムなキーを設定

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8888, debug=True)