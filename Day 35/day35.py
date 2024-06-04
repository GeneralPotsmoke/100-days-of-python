import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio!",
    from_='+1234567890',
    to='+0987654321'
)

print(message.sid)
