import unittest
import os
import tempfile
from app import app, get_db_connection, create_tables

class TestBitprop(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = os.urandom(24)
        self.app = app.test_client()
        self.db, self.cursor = get_db_connection()
        create_tables()

    def tearDown(self):
        self.db.close()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to Bitprop</h1>', response.data)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Login</h2>', response.data)

    def test_valid_login(self):
        response = self.app.post('/login', data=dict(username='agent', password='password'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Dashboard', response.data)

    def test_invalid_login(self):
        response = self.app.post('/login', data=dict(username='invalid', password='invalid'), follow_redirects=True)
        self.assertIn(b'Invalid username or password', response.data)

    def test_logout(self):
        self.app.post('/login', data=dict(username='agent', password='password'), follow_redirects=True)
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Dashboard', response.data)

    

if __name__ == '__main__':
    unittest.main()
