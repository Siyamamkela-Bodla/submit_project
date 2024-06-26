import unittest
import os
import tempfile
from app import app, get_db_connection, create_tables

class TestBitprop(unittest.TestCase):
    """
    Unit tests for the Bitprop Flask application.
    """

    def setUp(self):
        """
        Set up test environment.
        """
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = os.urandom(24)
        self.app = app.test_client()
        self.db, self.cursor = get_db_connection()
        create_tables()

    def tearDown(self):
        """
        Tear down test environment.
        """
        self.db.close()

    def test_home_page(self):
        """
        Test home page accessibility.
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to Bitprop</h1>', response.data)

    def test_login_page(self):
        """
        Test login page accessibility.
        """
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Login</h2>', response.data)

    def test_valid_login(self):
        """
        Test valid login credentials.
        """
        response = self.app.post('/login', data=dict(username='agent', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_invalid_login(self):
        """
        Test invalid login credentials.
        """
        response = self.app.post('/login', data=dict(username='invalid', password='invalid'), follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

    def test_logout(self):
        """
        Test logout functionality.
        """
        self.app.post('/login', data=dict(username='agent', password='password'), follow_redirects=True)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Dashboard', response.data)

if __name__ == '__main__':
    unittest.main()
