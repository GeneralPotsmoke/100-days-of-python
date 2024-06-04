#### Day 57: Templating with Jinja and Blog Project
**Challenge:** Create a Flask web application with a blog, using Jinja templates to render posts.

```python
from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"title": "Post 1", "content": "This is the content of post 1."},
    {"title": "Post 2", "content": "This is the content of post 2."}
]

@app.route('/')
def home():
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/blog.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
</head>
<body>
    <h1>My Blog</h1>
    {% for post in posts %}
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
    {% endfor %}
</body>
</html>
```


