#### Day 96: Portfolio Project - An eCommerce website with payment processing
**Challenge:** Create an eCommerce website with payment processing using Flask and Stripe.


```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>eCommerce Website</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">eCommerce Website</h1>
        <div class="card">
            <div class="card-body">
                <h3 class="card-title">T-shirt</h3>
                <p class="card-text">$20.00</p>
                <form action="/checkout" method="POST">
                    <button type="submit" class="btn btn-primary">Buy Now</button>
                </form>
            </div>
        </div>
    </div>
</body>
</html>
```

```html
<!-- templates/success.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Success</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Payment Successful</h1>
        <p>Your payment was successful. Thank you for your purchase!</p>
    </div>
</body>
</html>
```

```html
<!-- templates/cancel.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cancel</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container">
        <h1 class="my-4 text-center">Payment Cancelled</h1>
        <p>Your payment was cancelled. Please try again.</p>
    </div>
</body>
</html>
```


