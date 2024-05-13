# Bitprop Tenant Registration System

This project implements a tenant registration system for Bitprop, a real estate company. The system allows prospective tenants to view available properties, register their interest for specific properties, and notifies agents responsible for the relevant properties via email. The system is implemented in Python and uses SQLite for data storage.

## Project Structure

- `app.py`: Main Flask application file.
- `templates/`: HTML templates for rendering web pages.
- `static/`: Static files (CSS, JavaScript, images) for the frontend.
- `database.py`: Database management functions.
- `email_handler.py`: For handling emails.

## Dependencies

This project relies on the following Python packages:
- `sqlite3`: Standard library module for SQLite database interaction.
- `sendGrid`: Standard library module for sending emails via sendgrid.



These dependencies are included in the Python standard library and do not require separate installation.

## Setup

1. Clone the repository: `git clone https://github.com/Siyamamkela-Bodla/submit_project.git`
2. Install any additional dependencies: None required for this project.
3. Run the application: `python app.py`, `http://127.0.0.1:5000/`

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
- `inquiries`: Stores inquiries made by tenants for properties, including the property ID, name, and email of the tenant.

## Struggles Faced

- `Difficulty setting up database connections`: Encountered errors when querying data. Resolved by carefully reviewing documentation.

- `Setting up SendGrid account`: Faced challenges during the setup of the SendGrid account for email notifications. Encountered authentication errors and issues with API configuration. Resolved by carefully following the documentation and reaching out to SendGrid support for assistance.

- `Dashboard redirection after login`: Despite implementing session management and redirection logic, faced issues with redirection to the agent dashboard after successful login. Despite the implementation being in place, the issue persisted, indicating that there might be underlying factors contributing to the problem beyond what was initially addressed. 

## Additional Notes

- Error handling: The code includes robust error handling to handle exceptions during database interactions and email sending.
- Logging: Logging functionality can be added to log application events and errors for debugging purposes.
- Security: Ensure proper security measures are implemented, such as secure password storage and data encryption.


