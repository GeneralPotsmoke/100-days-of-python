#### Day 62: Flask, WTForms, Bootstrap and CSV - Coffee & Wifi Project
**Challenge:** Create a Flask application to submit and display information about coffee shops with wifi, using WTForms, Bootstrap, and CSV for data storage.

```python
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
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coffee & Wifi</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Welcome to Coffee & Wifi</h1>
        <a href="/add" class="btn btn-primary">Add a new cafe</a>
        <a href="/cafes" class="btn btn-secondary">View all cafes</a>
    </div>
</body>
</html>
```

```html
<!-- templates/add.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add a Cafe</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Add a Cafe</h1>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.cafe.label(class="form-control-label") }}
                {{ form.cafe(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.location.label(class="form-control-label") }}
                {{ form.location(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.open_time.label(class="form-control-label") }}
                {{ form.open_time(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.close_time.label(class="form-control-label") }}
                {{ form.close_time(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.coffee_rating.label(class="form-control-label") }}
                {{ form.coffee_rating(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.wifi_rating.label(class="form-control-label") }}
                {{ form.wifi_rating(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.power_rating.label(class="form-control-label") }}
                {{ form.power_rating(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```

```html
<!-- templates/cafes.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Cafes</title>
    <

link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">All Cafes</h1>
        <table class="table table-striped">
            <thead>
                <tr>
                    <th>Cafe</th>
                    <th>Location</th>
                    <th>Open</th>
                    <th>Close</th>
                    <th>Coffee</th>
                    <th>Wifi</th>
                    <th>Power</th>
                </tr>
            </thead>
            <tbody>
                {% for cafe in cafes %}
                <tr>
                    <td>{{ cafe[0] }}</td>
                    <td><a href="{{ cafe[1] }}">Location</a></td>
                    <td>{{ cafe[2] }}</td>
                    <td>{{ cafe[3] }}</td>
                    <td>{{ cafe[4] }}</td>
                    <td>{{ cafe[5] }}</td>
                    <td>{{ cafe[6] }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
</body>
</html>
```


