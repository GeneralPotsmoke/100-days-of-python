from twilio.rest import Client

def send_whatsapp_message(to, body):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
        body=body,
        from_='whatsapp:+14155238886',
        to=f'whatsapp:{to}'
    )
    print(f"Message sent: {message.sid}")

to = '+1234567890'
body = 'Hello, this is a test message from Python!'
send_whatsapp_message(to, body)
