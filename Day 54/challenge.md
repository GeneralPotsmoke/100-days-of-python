#### Day 54: Introduction to Web Development with Flask
**Challenge:** Create a basic Flask web application with a single route.

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)
```


