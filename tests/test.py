import unittest
from app import app

class TestBitprop(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Welcome to Bitprop</h1>', response.data)

    def test_login_page(self):
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h2>Login</h2>', response.data)

    def test_invalid_login(self):
        response = self.app.post('/login', data=dict(email='invalid@example.com', password='invalid'), follow_redirects=True)
        self.assertIn(b'Invalid email or password', response.data)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
