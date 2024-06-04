#### Day 88: Portfolio Project - Built a todo list website with Flask
**Challenge:** Create a Flask web application for a todo list. Use a SQLite database to store the tasks.

```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

@app.route('/')
def home():
    todos = Todo.query.all()
    return render_template('todos.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form['task']
    new_todo = Todo(task=task)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

```html
<!-- templates/todos.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Todo List</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Todo List</h1>
        <form method="POST" action="/add" class="form-inline my-4">
            <input type="text" name="task" class="form-control mr-2" placeholder="New Task">
            <button type="submit" class="btn btn-primary">Add Task</button>
        </form>
        <ul class="list-group">
            {% for todo in todos %}
            <li class="list-group-item d-flex justify-content-between align-items-center">


                {{ todo.task }}
                <a href="/delete/{{ todo.id }}" class="btn btn-danger btn-sm">Delete</a>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```


