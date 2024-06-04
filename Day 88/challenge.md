#### Day 88: Portfolio Project - Built a todo list website with Flask
**Challenge:** Create a Flask web application for a todo list. Use a SQLite database to store the tasks.


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


