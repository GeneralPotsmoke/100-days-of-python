from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {"title": "Post 1", "content": "This is the content of post 1."},
    {"title": "Post 2", "content": "This is the content of post 2."}
]

@app.route('/')
def home():
    return render_template('blog.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)
