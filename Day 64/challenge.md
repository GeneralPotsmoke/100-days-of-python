#### Day 64: My Top 10 Movies Website
**Challenge:** Create a website that lists your top 10 favorite movies using Flask and SQLAlchemy.

```python
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)

@app.route('/')
def home():
    movies = Movie.query.order_by(Movie.year.desc()).limit(10).all()
    return render_template('movies.html', movies=movies)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
```

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


