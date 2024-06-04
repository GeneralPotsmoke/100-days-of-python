#### Day 61: Building Advanced Forms with WTForms
**Challenge:** Use WTForms to create a more advanced form in your Flask application.

```python
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

class InfoForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def home():
    form = InfoForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        return f"Hello, {name}! Your email is {email}."
    return render_template('wtform.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/wtform.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WTForm</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Submit Your Info</h1>
        <form method="POST">
            {{ form.hidden_tag() }}
            <div class="form-group">
                {{ form.name.label(class="form-control-label") }}
                {{ form.name(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.email.label(class="form-control-label") }}
                {{ form.email(class="form-control") }}
            </div>
            <div class="form-group">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
</body>
</html>
```


