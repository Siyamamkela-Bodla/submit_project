import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Function to send email notification
def send_email_notification(agent_email, property_name, tenant_name, tenant_email):
    message = Mail(
        from_email='mamkela93@gmail.com',
        to_emails=agent_email,
        subject='New Tenant Inquiry',
        html_content=f'<strong>Property:</strong> {property_name}<br><strong>Tenant Name:</strong> {tenant_name}<br><strong>Tenant Email:</strong> {tenant_email}'
    )
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(str(e))


