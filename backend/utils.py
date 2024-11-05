from twilio.rest import Client
from flask import current_app as app

def send_sms(to_number, message_body):
    account_sid = app.config['TWILIO_ACCOUNT_SID']
    auth_token = app.config['TWILIO_AUTH_TOKEN']
    twilio_number = app.config['TWILIO_NUMBER']

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message_body,
        from_=twilio_number,
        to=to_number
    )
    return message.sid
