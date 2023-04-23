import unittest
from flask import json
from app import app, menu, messages

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to the Cafe', response.data)

    def test_order_get(self):
        response = self.app.get('/order')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Place your order', response.data)

    def test_order_post(self):
        response = self.app.post('/order', data={
            "name": "John Doe",
            "student_id": "12345",
            "items": ["coffee", "croissant"]
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for you order, John Doe (12345)! Your order has been placed. Your total is $5.48.', response.data)

    def test_chat_get(self):
        response = self.app.get('/chat')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your username', response.data)

    def test_chat_post(self):
        response = self.app.post('/chat', data={
            "username": "JohnDoe"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome, JohnDoe!', response.data)

    def test_send_message(self):
        response = self.app.post('/send', data={
            "username": "JohnDoe",
            "message": "Hello, world!"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, world!', response.data)
        self.assertIn(("JohnDoe", "Hello, world!"), messages)

if __name__ == '__main__':
    unittest.main()
