#### Day 56: Rendering HTML/Static Files and Name Card Project
**Challenge:** Create a Flask web application that serves HTML and static files, including a personal name card page.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/card')
def card():
    return render_template('card.html')

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <a href="/card">View My Name Card</a>
</body>
</html>
```

```html
<!-- templates/card.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Name Card</title>
</head>
<body>
    <h1>My Name Card</h1>
    <p>Name: John Doe</p>
    <p>Email: john@example.com</p>
</body>
</html>
```


