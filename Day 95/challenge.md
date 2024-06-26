#### Day 95: Portfolio Project - Built a custom website using an API
**Challenge:** Create a website that fetches data from a public API and displays it. Use Flask and a public API like the OpenWeatherMap API.


```html
<!-- templates/weather.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Weather App</h1>
        <form method="POST" class="form-inline my-4 justify-content-center">
            <input type="text" name="city" class="form-control mr-2" placeholder="Enter city name">
            <button type="submit" class="btn btn-primary">Get Weather</button>
        </form>
        {% if weather_data %}
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">{{ weather_data['name'] }}</h3>
                <p class="card-text">Temperature: {{ weather_data['main']['temp'] }} &deg;C</p>
                <p class="card-text">Weather: {{ weather_data['weather'][0]['description'] }}</p>
                <p class="card-text">Humidity: {{ weather_data['main']['humidity'] }}%</p>
                <p class="card-text">Wind Speed: {{ weather_data['wind']['speed'] }} m/s</p>
            </div>
        </div>
        {% endif %}
    </div>
</body>
</html>
```


