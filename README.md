# disaster-sms-alert
# SMS-Based Health Alert and Emergency Response System

## Overview

This project is a prototype of an **SMS-Based Health Alert and Emergency Response System** designed to serve rural areas with limited internet access, specifically targeting communities in Nepal. The system leverages SMS technology to disseminate health alerts, receive emergency requests, and provide essential health education, ensuring accessibility even in regions with basic mobile connectivity.

## Features

- **Real-time Health and Safety Alerts**: Broadcast concise SMS alerts about health hazards, natural disasters, and other emergencies to pre-registered users based on their location.
- **Two-Way Communication for Emergency Reporting**: Allow individuals to send predefined SMS codes (e.g., "HELP" or "EMERGENCY") to request assistance, automatically routing these to the nearest health center or emergency responders.
- **Automatic Emergency Response Routing**: Forward emergency requests to healthcare professionals or authorities in the area via SMS or email.
- **Broadcast Health Education**: Periodically send out health tips, warnings, or first-aid instructions via SMS to educate and inform users.
- **No Internet Required for Users**: Designed to work over SMS, ensuring accessibility even without internet connectivity.

## Technology Stack

- **Programming Language**: Python
- **Framework**: Flask
- **SMS Gateway**: Twilio
- **Database**: SQLite (can be upgraded to PostgreSQL for scalability)
- **Front-End (Admin Interface)**: Flask Templates with Flask-WTF for forms

## Prerequisites

- **Python 3.x** installed on your system
- **Twilio Account** with a registered phone number capable of sending and receiving SMS
- Basic understanding of **Python** and **Flask**
- Internet connection for server deployment (users only need SMS access)

## Installation

1. ### **Clone the Repository**

   ```bash
   git clone https://github.com/lifee77/disaster-sms-alert.git
   cd disaster-sms-alert
   ```

2. ### **Create a Virtual Environment (Optional but Recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. ### **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

4. ### **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your configuration:

   ```env
   SECRET_KEY=your_secret_key
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   TWILIO_NUMBER=your_twilio_phone_number
   ```

5. ### **Initialize the Database**

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

   If not using Flask-Migrate:

   ```python
   from app import db
   db.create_all()
   ```

6. ### **Configure Twilio Webhook**

   In your Twilio console, set the messaging webhook URL to:

   ```
   https://yourdomain.com/sms
   ```

   Replace `yourdomain.com` with your server's domain or IP address.

## Configuration

- **Flask App Configuration**: Modify `config.py` or the configuration section in `app.py` as needed.
- **Database URI**: Ensure `SQLALCHEMY_DATABASE_URI` points to your database.
- **Responder and User Data**: Populate the database with initial data for users and responders.

## Usage

1. ### **Running the Application**

   ```bash
   flask run
   ```

   By default, the application runs on `http://127.0.0.1:5000/`.

2. ### **Accessing the Admin Interface**

   Navigate to:

   ```
   http://127.0.0.1:5000/admin
   ```

   Here, administrators can:

   - Send health alerts to users in specific regions.
   - View and manage emergency requests.
   - Manage user and responder data.

3. ### **Sending Health Alerts**

   - Click on "Send Health Alert" in the admin dashboard.
   - Enter the region and the alert message.
   - Submit the form to broadcast the message.

4. ### **Users Sending Emergency Requests**

   - Users send an SMS with the word "HELP" or "EMERGENCY" to the Twilio number.
   - The system logs the request and forwards it to responders.
   - Users receive a confirmation SMS.

5. ### **Responders Receiving Alerts**

   - Responders receive an SMS or email with details of the emergency.
   - They can take appropriate action based on the information received.

## Testing

- **Simulate Incoming SMS**: Use Twilio's testing tools or send an SMS from a mobile device to test the system.
- **Unit Tests**: Implement unit tests for critical components to ensure reliability.

## Contributing

Contributions are welcome! Please follow the standard GitHub workflow:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## Contact Information

- **Project Maintainer**: [Your Name](mailto:your.email@example.com)

## Acknowledgements

- **Twilio**: For providing the SMS gateway services.
- **Flask**: For the lightweight web framework.
- **Flask-WTF**: For form handling in the admin interface.

## Future Enhancements

- **User Registration Interface**: Allow users to register via SMS or a web form.
- **Authentication**: Secure the admin interface with user authentication.
- **Geolocation Integration**: Incorporate location data for precise emergency response.
- **Multi-language Support**: Provide support for multiple languages.
- **Scalability Improvements**: Upgrade to PostgreSQL and optimize for higher loads.
- **Logging and Monitoring**: Implement logging mechanisms and monitoring tools.

## Troubleshooting

- **SMS Not Received**:

  - Verify that the phone numbers are correct and properly formatted.
  - Check Twilio's logs for any delivery issues.
  - Ensure your Twilio balance is sufficient.

- **Emergency Requests Not Forwarded**:

  - Confirm that responders are registered and associated with the correct regions.
  - Check for errors in the application's logs.

- **Application Errors**:

  - Run the application in debug mode to get detailed error messages.
  - Check the console output where the Flask app is running.

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Twilio Python Helper Library](https://www.twilio.com/docs/libraries/python)
- [Flask-WTF Documentation](https://flask-wtf.readthedocs.io/)

