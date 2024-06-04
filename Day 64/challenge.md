#### Day 64: My Top 10 Movies Website
**Challenge:** Create a website that lists your top 10 favorite movies using Flask and SQLAlchemy.


```html
<!-- templates/movies.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Top 10 Movies</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">My Top 10 Movies</h1>
        <ul class="list-group">
            {% for movie in movies %}
            <li class="list-group-item">
                <h2>{{ movie.title }} ({{ movie.year }})</h2>
                <p>{{ movie.description }}</p>
            </li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
```


