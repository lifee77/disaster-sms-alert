from flask import Flask
from .models import db

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sms_system.db'
    app.config['SECRET_KEY'] = 'your_secret_key'
    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .routes import app as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app