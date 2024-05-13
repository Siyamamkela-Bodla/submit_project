import sqlite3
from flask import Flask, redirect, render_template, request, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Add a secret key for session management

# properties
properties = [
    {"name": "Apartment 1", "agent_id": 1},
    {"name": "Apartment 2", "agent_id": 2},
    {"name": "Apartment 3", "agent_id": 3},
    {"name": "Apartment 4", "agent_id": 4},
    {"name": "House 1", "agent_id": 1},
    {"name": "House 2", "agent_id": 2},
    {"name": "House 3", "agent_id": 3},
    {"name": "House 4", "agent_id": 4},
]

# Define a fake agent login for demonstration purposes
agents = [
    {"email": "agent1@example.com", "password": "password1"},
    {"email": "agent2@example.com", "password": "password2"}
]

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', properties=properties)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Check if the provided email and password match any agent credentials
        for agent in agents:
            if agent['email'] == email and agent['password'] == password:
                # If the credentials match, set session and redirect to the dashboard
                session['logged_in'] = True
                return redirect(url_for('dashboard'))

        # If no matching agent is found, redirect back to the login page
        return redirect(url_for('login'))

    # If it's a GET request, render the login page
    return render_template('login.html')  # Assuming you have a login.html template

# Route for the agent dashboard
@app.route('/dashboard')
def dashboard():
    if 'logged_in' not in session:
        return redirect(url_for('login'))
    
    # You can access session['agent_id'] or session['agent_username'] here
    return render_template('dashboard.html')

# Route handler for the "/properties" endpoint
@app.route('/properties')
def get_properties():
    return render_template('properties.html', properties=properties)

if __name__ == '__main__':
    app.run(debug=True)
