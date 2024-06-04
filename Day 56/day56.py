from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/card')
def card():
    return render_template('card.html')

if __name__ == '__main__':
    app.run(debug=True)
