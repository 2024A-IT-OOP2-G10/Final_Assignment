from flask import Blueprint, render_template, request, redirect, url_for
from models.todo import Todo

todo_bp = Blueprint('todo', __name__, url_prefix='/todo')

@todo_bp.route('/', methods=['GET', 'POST'])
def todo_form():
    if request.method == 'POST':
        name = request.form.get('name')
        todo = request.form.get('todo')
        date = request.form.get('date')

        return redirect(url_for('todo.todo_result', name=name, todo=todo, date=date))

    return render_template('todo.html')

@todo_bp.route('/result', methods=['GET', 'POST'])
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
