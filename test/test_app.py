import unittest
import requests

class Bio_test(unittest.TestCase):
    def test_Bio(self):
        endpoint = requests.get("https://hng9-bio.herokuapp.com/")
        assert endpoint.status_code == 200
        assert endpoint.text == "OK"
