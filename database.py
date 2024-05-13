import os
import sqlite3
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from werkzeug.security import generate_password_hash

app = Flask(__name__)
# Generate a secure secret key
secret_key = os.urandom(24)
app.secret_key = secret_key

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('bitprop.db')
    return conn, conn.cursor()

# Function to close database connection
def close_db_connection(conn):
    conn.close()

# Function to create database tables if not exists
def create_tables():
    conn, cursor = get_db_connection()
    cursor.execute('''CREATE TABLE IF NOT EXISTS properties (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        agent_id INTEGER NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS inquiries (
                        id INTEGER PRIMARY KEY,
                        property_id INTEGER,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        FOREIGN KEY (property_id) REFERENCES properties(id)
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS agents (
                        id INTEGER PRIMARY KEY,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL,
                        email TEXT
                    )''')
    conn.commit()
    close_db_connection(conn)

# Initialize database tables
create_tables()

# Route for the home page
@app.route('/')
def home():
    conn, cursor = get_db_connection()
    cursor.execute("SELECT * FROM properties")
    properties = cursor.fetchall()
    close_db_connection(conn)
    return render_template('index.html', properties=properties)

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if username and password are valid (dummy check for demo)
        if username == 'agent' and password == 'password':
            session['logged_in'] = True
            session['agent_id'] = 1  # Replace with actual agent ID from database
            return redirect(url_for('dashboard.html', agent_id=session['agent_id']))  # Redirect to the dashboard
        else:
            return render_template('login.html', error='Invalid username or password')
    
    return render_template('login.html')

# Route for the agent dashboard
@app.route('/dashboard/<agent_id>')
def dashboard(agent_id):
    if 'logged_in' not in session or int(agent_id) != session.get('agent_id'):
        return redirect(url_for('login'))

    conn, cursor = get_db_connection()
    cursor.execute("SELECT * FROM inquiries WHERE property_id IN (SELECT id FROM properties WHERE agent_id=?)", (agent_id,))
    agent_inquiries = cursor.fetchall()
    close_db_connection(conn)
    return render_template('dashboard.html', inquiries=agent_inquiries)

# Route to handle tenant inquiries
@app.route('/submit_interest', methods=['POST'])
def submit_interest():
    if 'logged_in' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    
    property_id = request.form['property_id']
    name = request.form['name']
    email = request.form['email']
    
    # Insert inquiry into database
    conn, cursor = get_db_connection()
    cursor.execute("INSERT INTO inquiries (property_id, name, email) VALUES (?, ?, ?)", (property_id, name, email))
    conn.commit()
    close_db_connection(conn)
    
    return jsonify({"message": "Inquiry submitted successfully"}), 200

# Route to logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# Route for agent registration
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username is already taken
        conn, cursor = get_db_connection()
        cursor.execute("SELECT * FROM agents WHERE username=?", (username,))
        existing_agent = cursor.fetchone()
        if existing_agent:
            close_db_connection(conn)
            return render_template('register.html', error='Username already taken')
        
        # Hash the password before storing it
        hashed_password = generate_password_hash(password)
        
        # Insert the new agent into the database
        cursor.execute("INSERT INTO agents (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        close_db_connection(conn)
        
        return redirect(url_for('login'))
    
    return render_template('register.html')

# Route for agent dashboard to manage properties
@app.route('/dashboard/manage_properties')
def manage_properties():
    if 'logged_in' not in session:
        return redirect(url_for('login'))

    conn, cursor = get_db_connection()
    cursor.execute("SELECT * FROM properties WHERE agent_id=?", (session['agent_id'],))
    agent_properties = cursor.fetchall()
    close_db_connection(conn)
    return render_template('manage_properties.html', properties=agent_properties)

# Route for adding a new property
@app.route('/add_property', methods=['POST'])
def add_property():
    if 'logged_in' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    
    name = request.form['name']
    
    # Insert property into database
    conn, cursor = get_db_connection()
    cursor.execute("INSERT INTO properties (name, agent_id) VALUES (?, ?)", (name, session['agent_id']))
    conn.commit()
    close_db_connection(conn)
    
    return redirect(url_for('manage_properties'))

# Route for deleting a property
@app.route('/delete_property/<property_id>', methods=['POST'])
def delete_property(property_id):
    if 'logged_in' not in session:
        return jsonify({"message": "Unauthorized"}), 401
    
    # Delete property from database
    conn, cursor = get_db_connection()
    cursor.execute("DELETE FROM properties WHERE id=? AND agent_id=?", (property_id, session['agent_id']))
    conn.commit()
    close_db_connection(conn)
    
    return redirect(url_for('manage_properties'))

if __name__ == '__main__':
    app.run(debug=True)
