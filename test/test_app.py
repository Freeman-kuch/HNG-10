import unittest
import requests

class Bio_test(unittest.TestCase):
    def test_Bio(self):
        endpoint = requests.get("http://127.0.0.1:5000/bio?slack_name=freeman&track=backend")  
        # the url should be changed once deployed to live servere
        assert endpoint.status_code == 200
        assert endpoint.text == "OK"
