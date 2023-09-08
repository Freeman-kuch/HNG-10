import unittest
import requests

class Bio_test(unittest.TestCase):
    def test_Bio(self):
        endpoint = requests.get("https://hng-10.up.railway.app/api?slack_name=Freeman&track=backend")  
        assert endpoint.status_code == 200


# python -m unittest test_app.py to run from CLI