from flask import Blueprint, render_template, request, redirect, url_for, flash
from backend.forms import AlertForm
from backend.models import User, Responder, EmergencyRequest
from app import db
from backend.utils import send_sms
from twilio.twiml.messaging_response import MessagingResponse
from flask import current_app as app
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return redirect(url_for('main.dashboard'))

@main.route('/dashboard', methods=['GET'])
def dashboard():
    region = request.args.get('region')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    query = EmergencyRequest.query

    if region:
        query = query.filter(EmergencyRequest.region.ilike(f"%{region}%"))
    if start_date:
        query = query.filter(EmergencyRequest.timestamp >= datetime.strptime(start_date, "%Y-%m-%d"))
    if end_date:
        query = query.filter(EmergencyRequest.timestamp <= datetime.strptime(end_date, "%Y-%m-%d"))

    emergency_requests = query.order_by(EmergencyRequest.timestamp.desc()).all()

    # Example data
    user_locations = [
        {'lat': 27.7172, 'lng': 85.3240},
        {'lat': 27.7000, 'lng': 85.3333}
    ]
    responder_locations = [
        {'lat': 27.7172, 'lng': 85.3240},
        {'lat': 27.7000, 'lng': 85.3333}
    ]
    emergency_requests = [
        {'user_phone': '1234567890', 'region': 'Kathmandu', 'message': 'Help needed', 'timestamp': datetime.now()},
        {'user_phone': '0987654321', 'region': 'Lalitpur', 'message': 'Emergency', 'timestamp': datetime.now()}
    ]
    return render_template('dashboard.html', 
                        user_locations=user_locations, 
                        responder_locations=responder_locations, 
                        emergency_requests=emergency_requests)


@main.route('/send_alert', methods=['GET', 'POST'])
def send_alert():
    form = AlertForm()
    if form.validate_on_submit():
        region = form.region.data
        message = form.message.data
        users = User.query.filter_by(region=region).all()
        for user in users:
            send_sms(user.phone_number, message)
        flash('Alert sent successfully!', 'success')
        return redirect(url_for('main.dashboard'))
    return render_template('send_alert.html', form=form)

@main.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming SMS with a confirmation and forward to responders."""
    incoming_msg = request.values.get('Body', '').strip().lower()
    from_number = request.values.get('From', '')
    user = User.query.filter_by(phone_number=from_number).first()
    region = user.region if user else 'Unknown'

    if incoming_msg in ['help', 'emergency']:
        # Log the emergency request
        emergency = EmergencyRequest(user_phone=from_number, region=region, message=incoming_msg)
        db.session.add(emergency)
        db.session.commit()

        # Forward to responders
        responders = Responder.query.filter_by(region=region).all()
        for responder in responders:
            alert_message = f"Emergency from {from_number} in {region}."
            send_sms(responder.phone_number, alert_message)

        # Respond to user
        resp = MessagingResponse()
        resp.message("Your emergency request has been received. Help is on the way.")
        return str(resp)
    else:
        # Non-emergency message
        resp = MessagingResponse()
        resp.message("Unrecognized command. Send 'HELP' or 'EMERGENCY' for assistance.")
        return str(resp)