from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Location URL', validators=[DataRequired()])
    open_time = StringField('Opening Time', validators=[DataRequired()])
    close_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = StringField('Coffee Rating', validators=[DataRequired()])
    wifi_rating = StringField('Wifi Rating', validators=[DataRequired()])
    power_rating = StringField('Power Socket Rating', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafes.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow([form.cafe.data, form.location.data, form.open_time.data,
                                form.close_time.data, form.coffee_rating.data,
                                form.wifi_rating.data, form.power_rating.data])
        return 'Cafe added successfully!'
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    cafes = []
    with open('cafes.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            cafes.append(row)
    return render_template('cafes.html', cafes=cafes)

if __name__ == '__main__':
    app.run(debug=True)
