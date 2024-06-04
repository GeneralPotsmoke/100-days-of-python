#### Day 87: Portfolio Project - Built a website that lists cafes with wifi and power for remote working
**Challenge:** Create a Flask website that lists cafes with wifi and power for remote working. Use a SQLite database to store the cafe data.


```html
<!-- templates/cafes.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cafes</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Cafes with Wifi and Power</h1>
        <a href="/add" class="btn btn-primary">Add New Cafe</a>
        <ul class="list-group my-4">
            {% for cafe in cafes %}
            <li class="list-group-item">
                <h3>{{ cafe.name }}</h3>
                <p>Location: {{ cafe.location }}</p>
                <p>Wifi Rating: {{ cafe.wifi_rating }}</p>
                <p>Power Rating: {{ cafe.power_rating }}</p>
            </li>
            {% endfor %}
        </ul>
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
    <title>Add Cafe</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Add a New Cafe</h1>
        <form method="POST">
            <div class="form-group">
                <label for="name">Cafe Name:</label>
                <input type="text" id="name" name="name" class="form-control">
            </div>
            <div class="form-group">
                <label for="location">Location:</label>
                <input type="text" id="location" name="location" class="form-control">
            </div>
            <div class="form-group">
                <label for="wifi_rating">Wifi Rating:</label>
                <input type="number" id="wifi_rating" name="wifi_rating" class="form-control" min="1" max="5">
            </div>
            <div class="form-group">
                <label for="power_rating">Power Rating:</label>
                <input type="number" id="power_rating" name="power_rating" class="form-control" min="1" max="5">
            </div>
            <button type="submit" class="btn btn-primary">Add Cafe</button>
        </form>
    </div>
</body>
</html>
```


