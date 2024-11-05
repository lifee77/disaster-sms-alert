from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    region = db.Column(db.String(50), nullable=False)
    registered_on = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.phone_number}>'

class Responder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), unique=True, nullable=False)
    region = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Responder {self.name}>'

class EmergencyRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_phone = db.Column(db.String(15), nullable=False)
    region = db.Column(db.String(50), nullable=False)
    message = db.Column(db.String(160))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<EmergencyRequest from {self.user_phone}>'
