# Simple To-Do list CLI based application
# Taks involved in this app are :
# 1. Add Tasks
# 2. View Tasks
# 3. Delete Tasks
# 4. Clear Tasks

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# our task storage (same as your global "tasks" list)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/clear')
def clear_task():
    tasks.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
