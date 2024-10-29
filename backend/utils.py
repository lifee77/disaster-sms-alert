from twilio.rest import Client
from .models import User

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'
client = Client(account_sid, auth_token)

def forward_emergency_request(region, user_number, message):
    responders = get_responders_by_region(region)
    for responder in responders:
        client.messages.create(
            body=f"Emergency Alert from {user_number}: {message}",
            from_=twilio_number,
            to=responder.phone_number
        )

def send_health_alert(region, alert_message):
    users = User.query.filter_by(region=region).all()
    for user in users:
        client.messages.create(
            body=alert_message,
            from_=twilio_number,
            to=user.phone_number
        )

def get_responders_by_region(region):
    return Responder.query.filter_by(region=region).all()