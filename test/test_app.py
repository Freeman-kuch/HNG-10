import unittest
import requests

class Bio_test(unittest.TestCase):
    def test_Bio(self):
        endpoint = requests.get("https://hng-10.up.railway.app/bio?slack_name=Freeman&track=Backend track")  
        # the url should be changed once deployed to live servere
        assert endpoint.status_code == 200
        assert endpoint.text == "OK"
