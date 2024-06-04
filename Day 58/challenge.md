#### Day 58: Bootstrap
**Challenge:** Add Bootstrap to your Flask blog application for better styling and responsiveness.

```html
<!-- templates/blog.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blog</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="container">
    <h1 class="my-4">My Blog</h1>
    {% for post in posts %}
        <div class="card my-3">
            <div class="card-body">
                <h2 class="card-title">{{ post.title }}</h2>
                <p class="card-text">{{ post.content }}</p>
            </div>
        </div>
    {% endfor %}
</body>
</html>
```


