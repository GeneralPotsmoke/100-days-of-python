from flask import Flask, render_template_string, request
import random

app = Flask(__name__)
number_to_guess = random.randint(1, 100)

@app.route('/')
def home():
    return render_template_string("""
    <h1>Guess the Number</h1>
    <form action="/guess" method="POST">
        <input type="number" name="guess">
        <button type="submit">Submit</button>
    </form>
    """)

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    if guess < number_to_guess:
        return "Higher!"
    elif guess > number_to_guess:
        return "Lower!"
    else:
        return "Congratulations, you guessed the number!"

if __name__ == '__main__':
    app.run(debug=True)
