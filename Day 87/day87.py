from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(app)

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(300), nullable=False)
    wifi_rating = db.Column(db.Integer, nullable=False)
    power_rating = db.Column(db.Integer, nullable=False)

@app.route('/')
def home():
    cafes = Cafe.query.all()
    return render_template('cafes.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form['name']
        location = request.form['location']
        wifi_rating = int(request.form['wifi_rating'])
        power_rating = int(request.form['power_rating'])
        new_cafe = Cafe(name=name, location=location, wifi_rating=wifi_rating, power_rating=power_rating)
        db.session.add(new_cafe)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
