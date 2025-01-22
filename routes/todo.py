from flask import Blueprint, render_template, request, redirect, url_for
from models.todo import Todo
from models import data

todos_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todos_bp.route('/', methods=['GET', 'POST'])
def todo_form():
    if request.method == 'POST':
        name = request.form.get('name')
        todo = request.form.get('todo')
        date = request.form.get('date')

        return redirect(url_for('todo.todo_result', name=name, todo=todo, date=date))

    return render_template('todo.html')

@todos_bp.route('/result', methods=['GET', 'POST'])
def todo_result():
    if request.method == 'POST':
        name = request.form.get('name')
        todo = request.form.get('todo')
        date = request.form.get('date')

        new_todo = Todo(name=name, todo=todo, time=date)
        new_todo.save()

        return redirect(url_for('home'))

    return render_template('todo_result.html', name=request.args.get('name'),
                           todo=request.args.get('todo'), date=request.args.get('date'))



@todos_bp.route('', methods=['GET', 'POST', 'DELETE'])
def todos():
    if request.method == 'GET':
        # todos = [
        #             {
        #                 "todo_id": 1,
        #                 "lecture_title": "情報システム演習",
        #                 "description": "課題1の内容",
        #                 "deadline": "2024-12-10 20:29:57.744098"
        #             },
        #             {
        #                 "todo_id": 2,
        #                 "lecture_title": "オブジェクト演習",
        #                 "description": "課題2の内容",
        #                 "deadline": "2024-12-10 20:29:57.744098"
        #             }
        #         ]
        return render_template('todo_result.html', todos=data.todos)
    elif request.method == 'POST':
        user_id = request.form['user_id']
        lecture_id = request.form['lecture_id']
        description = request.form['description']
        deadline = request.form['deadline']
        
        #データベースの追加処理
        
        # "user_id": 1,
        # "lecture_id": 1,
        # "description": "課題1の内容",
        # "deadline": "2024-12-10 20:29:57.744098"
        
        ans = {"success": "todoDBへの登録に成功しました"}
        return render_template('todo.html', ans=ans)
    
    elif request.method == 'DELETE':
       user_id = 1
       todo_id = 1
       #データベースの削除処理 
       ans = {"success": "todoDBの削除に成功しました"}
       return render_template('todo.html', ans=ans)