from flask import Flask, request, redirect, render_template, url_for
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from .models import db, User, EmergencyRequest
from .forms import AlertForm
from .utils import forward_emergency_request, send_health_alert

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sms_system.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
twilio_number = 'your_twilio_number'
client = Client(account_sid, auth_token)

@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.values.get('Body', '').strip().upper()
    from_number = request.values.get('From', '')
    user = User.query.filter_by(phone_number=from_number).first()

    if incoming_msg == 'HELP' or incoming_msg == 'EMERGENCY':
        emergency = EmergencyRequest(user_id=user.id, message=incoming_msg)
        db.session.add(emergency)
        db.session.commit()
        forward_emergency_request(user.region, from_number, incoming_msg)
        resp = MessagingResponse()
        resp.message("Your emergency request has been received. Help is on the way.")
        return str(resp)
    else:
        resp = MessagingResponse()
        resp.message("Invalid command. Send 'HELP' or 'EMERGENCY' for assistance.")
        return str(resp)

@app.route('/admin')
def admin_dashboard():
    return render_template('dashboard.html')

@app.route('/admin/send_alert', methods=['GET', 'POST'])
def send_alert():
    form = AlertForm()
    if form.validate_on_submit():
        region = form.region.data
        message = form.message.data
        send_health_alert(region, message)
        return redirect(url_for('admin_dashboard'))
    return render_template('send_alert.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)