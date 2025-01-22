from datetime import datetime
from flask import Blueprint, render_template, request, redirect, session, url_for
from flask_login import current_user, login_required
from models.lecture import Lecture
from models.todo import Todo
from models.db import db
from models.userLectureRelation import UserLectureRelation

todos_bp = Blueprint('todos', __name__, url_prefix='/todos')

@todos_bp.route('/', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        user_id = current_user.get_id()
        
        # DBからuser_idに一致する講義データを取得
        user_lecture_relations = UserLectureRelation.query.filter_by(user_id=user_id).all()
        lecture_ids = [relation.lecture_id for relation in user_lecture_relations]
        lectures = Lecture.query.filter(Lecture.id.in_(lecture_ids)).all()
        
        return render_template('todo.html', classes=lectures)
    
    elif request.method == 'POST':
        
        deadline = datetime.strptime(request.form['date'], '%Y-%m-%d')
        
        
        user_id = current_user.get_id()
        lecture_id = request.form['lecture']
        description = request.form['todo']
        deadline = deadline
        
        # DBからidに一致する講義データを取得
        lecture_title = Lecture.query.filter_by(id=lecture_id).first().title
        
        todoData = {
            "user_id": user_id,
            "lecture_id": lecture_id,
            "lecture_title": lecture_title,
            "description": description,
            "deadline": deadline
        }
        
        # sessionにtodoDataを保存
        session['todoData'] = todoData
        
        return render_template('todo_result.html', todoData=todoData)

@todos_bp.route('/result', methods=['POST', 'DELETE'])
@login_required
def result():
    if request.method == 'POST':
        # データ取得
        todoData = session.get('todoData')
        
        # DBに保存する処理
        newTodo = Todo(
            user_id=todoData['user_id'],
            lecture_id=todoData['lecture_id'],
            description=todoData['description'],
            deadline=todoData['deadline']
        )
        db.session.add(newTodo)
        db.session.commit()
        
        return redirect(url_for('home.index'))
    
    elif request.method == 'DELETE':
        todo_id = request.form.get('todo_id')
        todo = Todo.query.filter_by(id=todo_id).first()
        if todo:
            db.session.delete(todo)
            db.session.commit()
        
        return redirect(url_for('todos.index'))
    
    return render_template('todo.html')


def get_todo(user_id):

    # 本来はDBから講義データを取得する

    
    todos = db.session.query(
        Todo.id, Lecture.title, Todo.description, Todo.deadline
    ).join(Lecture, Todo.lecture_id == Lecture.id).filter(Todo.user_id == user_id).all()
            
    return todos