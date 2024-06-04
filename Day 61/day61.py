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
