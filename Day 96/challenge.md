#### Day 96: Portfolio Project - An eCommerce website with payment processing
**Challenge:** Create an eCommerce website with payment processing using Flask and Stripe.

```python
from flask import Flask, render_template, request, redirect, url_for
import stripe

app = Flask(__name__)

stripe_keys = {
    'secret_key': 'your_secret_key_here',
    'publishable_key': 'your_publishable_key_here'
}

stripe.api_key = stripe_keys['secret_key']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkout', methods=['POST'])
def checkout():
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency

': 'usd',
                'product_data': {
                    'name': 'T-shirt',
                },
                'unit_amount': 2000,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=url_for('success', _external=True),
        cancel_url=url_for('cancel', _external=True),
    )
    return redirect(session.url, code=303)

@app.route('/success')
def success():
    return render_template('success.html')

@app.route('/cancel')
def cancel():
    return render_template('cancel.html')

if __name__ == '__main__':
    app.run(debug=True)
```

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


