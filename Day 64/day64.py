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
