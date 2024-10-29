from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class AlertForm(FlaskForm):
    region = StringField('Region')
    message = StringField('Alert Message')
    submit = SubmitField('Send Alert')