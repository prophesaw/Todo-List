from flask import jsonify, request, render_template, redirect, url_for
from task_models import Task

def register_routes(app, db):

    @app.route('/')
    def index():
        tasks = Task.query.all()
        return render_template('index.html', tasks=tasks)

    @app.route('/task/add', methods=['POST'])
    def add_task():
        title = request.form.get('title')
        description = request.form.get('description')
        try:
            new_task = Task(title=title, description=description)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as e:
            return str(e)

    @app.route('/task/delete/<int:id>', methods=['GET', 'DELETE'])
    def delete_task(id):
        id = int(id)
        task = Task.query.get(id)
        
        try:
            if task:
               db.session.delete(task)
               db.session.commit()
               return redirect(url_for('index'))
            else:
                return 'Task not found'
        except Exception as e:
            return str(e)



