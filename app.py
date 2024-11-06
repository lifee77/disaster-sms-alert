from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from backend.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # Scheduler setup
    app.config['JOBS'] = [
        {
            'id': 'scheduled_health_tip',
            'func': 'app:send_scheduled_health_tip',
            'trigger': 'interval',
            'hours': 24
        }
    ]
    scheduler.init_app(app)
    scheduler.start()

    return app

def send_scheduled_health_tip():
    """Function to send periodic health tips to all users."""
    health_tip = "Remember to drink water and stay hydrated!"
    users = User.query.all()
    for user in users:
        send_sms(user.phone_number, health_tip)


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
