import unittest
from app import app


class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to Bitprop</h1>', response.data)

    def test_login_page_loads(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Login</h2>', response.data)

    def test_successful_login(self):
        response = self.app.post('/login', data={'email': 'agent1@example.com', 'password': 'password1'}, follow_redirects=True)
        self.assertIn(b'Dashboard', response.data)

    def test_unsuccessful_login(self):
        response = self.app.post('/login', data={'email': 'invalid@example.com', 'password': 'invalid'}, follow_redirects=True)
        self.assertIn(b'Login', response.data)
        self.assertIn(b'Invalid email or password', response.data)

    def test_dashboard_requires_login(self):
        response = self.app.get('/dashboard', follow_redirects=True)
        self.assertIn(b'Login', response.data)
        self.assertNotIn(b'Dashboard', response.data)

    def test_properties_page(self):
        response = self.app.get('/properties')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Properties</h2>', response.data)

if __name__ == '__main__':
    unittest.main()
