# Bitprop Tenant Registration System

This project implements a tenant registration system for Bitprop, a real estate company. The system allows prospective tenants to view available properties, register their interest for specific properties, and notifies agents responsible for the relevant properties via email. The system is implemented in Python and uses SQLite for data storage.

## Project Structure

- `database.py`: Contains the `Database` class responsible for database interactions.
- `email_service.py`: Contains the `EmailService` class responsible for sending email notifications.
- `main.py`: Contains the main logic of the application, including user authentication and handling user inputs.

## Dependencies

This project relies on the following Python packages:
- `sqlite3`: Standard library module for SQLite database interaction.
- `smtplib`: Standard library module for sending emails via SMTP.
- `email`: Standard library module for composing email messages.
- `email.mime.text`: Standard library module for creating MIME text parts for email messages.
- `email.mime.multipart`: Standard library module for creating MIME multipart messages for email messages.

These dependencies are included in the Python standard library and do not require separate installation.

## Setup

1. Clone the repository: `git clone https://github.com/Siyamamkela-Bodla/submit_project.git`
2. Install any additional dependencies: None required for this project.
3. Update the configuration in `config.py` with SMTP server details for email notifications.
4. Run the application: `python main.py`

## Usage

1. Prospective tenants can access the registration page on the Bitprop website.
2. They can view available properties and register their interest by providing their name and email.
3. Agents can log in to view registered tenants for properties they manage.
4. Agents will receive email notifications when tenants register interest in their properties.

## Database Schema

- `properties`: Stores information about properties, including name and agent ID.
- `agents`: Stores agent details, including username and password.
- `tenants`: Stores information about tenants, including full name and email.
- `registrations`: Links properties and tenants, indicating tenant interest in properties.

## Additional Notes

- Error handling: The code includes robust error handling to handle exceptions during database interactions and email sending.
- Logging: Logging functionality can be added to log application events and errors for debugging purposes.
- Security: Ensure proper security measures are implemented, such as secure password storage and data encryption.

## Contact Information For Bitprop

- Email: info@bitprop.com
- Website: www.bitprop.com
- Twitter: @bitpropza
