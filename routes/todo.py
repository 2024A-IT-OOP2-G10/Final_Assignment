from flask import Blueprint, render_template, request, redirect, session, url_for
from models.todo import Todo
from models import data

todos_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todos_bp.route('/', methods=['GET','POST'])

def index():
    
    # 本来はDBから講義データを取得する
    
    if request.method == 'GET':
    
        classes = [
        {
            "id": 1,
            "title": "情報システム演習",
        },
        {
            "id": 2,
            "title": "オブジェクト演習",
        },
        ]
    
    
        return render_template('todo.html', classes=classes)
    
    elif request.method == 'POST':
        
        user_id = session.get('user_id')
        lecture_id = request.form['lecture']
        description = request.form['todo']
        deadline = request.form['date']
        
        # DBからidに一致する講義データを取得
        
        
        # 仮のデータ
        lecture_title = "情報システム演習";

        
        
        todoData = {
            "user_id": user_id,
            "lecture_id": lecture_id,
            "lecture_title": lecture_title,
            "description": description,
            "deadline": deadline
        }
        
        # sessionにtodoDataを保存
        session['todoData'] = todoData

        
        
        ans = {"success": "todoDBへの登録に成功しました"}
        #result.htmlにリダイレクト
        return render_template('todo_result.html',todoData=todoData)
        

@todos_bp.route('/result',  methods=[ 'POST', 'DELETE'])
def result():
    
    
    if request.method == 'POST':
        
        # データ取得
        user_id = session.get('user_id')

        #sessionからtodoDataを取得
        todoData = session.get('todoData')

        
        # 本来はDBに保存する処理
        
        ans = {"success": "todoDBへの登録に成功しました"}
        
        return redirect(url_for('home.index'))
        
    elif request.method == 'DELETE':
        user_id = 1
        todo_id = 1
        #データベースの削除処理
        ans = {"success": "todoDBの削除に成功しました"}
        return render_template(url_for('todos.result'), ans=ans)
    
    return render_template('todo.html')




def get_todo(user_id):

    # 本来はDBから講義データを取得する

    
            todos = data.todos
            
            return todos
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
    


# @todos_bp.route('/result', methods=['GET', 'POST'])
# def result():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         todo = request.form.get('todo')
#         date = request.form.get('date')

#         new_todo = Todo(name=name, todo=todo, time=date)
#         new_todo.save()

#         return redirect(url_for('home'))

#     return render_template('todo_result.html', name=request.args.get('name'),
#                            todo=request.args.get('todo'), date=request.args.get('date'))
