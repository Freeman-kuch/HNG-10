import unittest
from flask import Flask
from your_app import app  # Replace "your_app" with the actual import path of your Flask app
from resource.endpoints import bio, stage_2

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_config(self):
        # Test app configuration
        self.assertEqual(app.config['SQLALCHEMY_TRACK_MODIFICATIONS'], False)

    def test_resource_registration(self):
        # Test if resources are registered correctly
        with self.app as client:
            response_bio = client.get("/api")
            response_stage_2 = client.get("/api/1")  # Replace "1" with a valid user_id
            self.assertEqual(response_bio.status_code, 200)
            self.assertEqual(response_stage_2.status_code, 200)  # Adjust this based on your endpoint behavior

    def test_hello_world(self):
        # Test a basic endpoint
        with self.app as client:
            response = client.get("/")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Hello, World!", response.data)

if __name__ == "__main__":
    unittest.main()
