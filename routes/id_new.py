# Blueprintの作成
from flask import Blueprint, render_template

user_bp = Blueprint('new', __name__, url_prefix='/new')

# TODO:ここの実装

@user_bp.route('/home', methods=['GET', 'POST'])
def add():
    
    # if request.method == 'POST':
    #     name = request.form['name']
    #     age = request.form['age']
    #     User.create(name=name, age=age)
    #     return redirect(url_for('user.list'))
    
    return render_template('home.html')
