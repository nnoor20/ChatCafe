import unittest
from flask import json
from app import app, menu, rooms, socketio
from flask_socketio import SocketIOTestClient
import time

class TestFlaskApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.socketio_test_client = SocketIOTestClient(app, socketio)

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'MSU Denver Chat Cafe', response.data)

    def test_order_get(self):
        response = self.app.get('/order')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Order Confirmation', response.data)

    def test_order_post(self):
        response = self.app.post('/order', data={
            "name": "John Doe",
            "student_id": "12345",
            "total_price1": "5.48",
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Thank you for you order, John Doe, (12345)! Your order has been placed. Your total is $5.48.', response.data)

    def test_index_get(self):
        response = self.app.get('/index')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter your username', response.data)
        
    def test_connect_and_send_message(self):
        self.socketio_test_client.connect()
        time.sleep(2)
        print("Connected:", self.socketio_test_client.is_connected())
        response = self.socketio_test_client.emit('message', {'data': 'Hello, world!'})
        
    def test_disconnect(self):
        self.socketio_test_client.connect()
        self.socketio_test_client.disconnect()
        response = self.socketio_test_client.is_connected()
        self.assertFalse(response)

if __name__ == '__main__':
    unittest.main()
