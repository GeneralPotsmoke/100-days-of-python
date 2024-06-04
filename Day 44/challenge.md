#### Day 44: Intermediate CSS
**Challenge:** Use advanced CSS features like flexbox, grid, and animations to enhance your page.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Advanced CSS Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            display: flex;


            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        h1 {
            color: #0056b3;
            animation: color-change 3s infinite;
        }
        p {
            line-height: 1.6;
        }
        a {
            color: #d9534f;
        }
        img {
            border: 2px solid #ccc;
            margin: 10px;
        }
        @keyframes color-change {
            0% { color: #0056b3; }
            50% { color: #d9534f; }
            100% { color: #0056b3; }
        }
    </style>
</head>
<body>
    <h1>Welcome to My Advanced CSS Page</h1>
    <p>Hello! I am learning web development. This is my first HTML page with advanced CSS styling.</p>
    <p>Check out <a href="https://www.example.com">this link</a> for more information.</p>
    <img src="image1.jpg" alt="Image 1" width="300">
</body>
</html>
```


