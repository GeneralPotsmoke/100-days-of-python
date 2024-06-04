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
