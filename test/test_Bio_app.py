import unittest
import requests

class Bio_test(unittest.TestCase):
    def Bio(self):
        endpoint = requests.get("")
        assert endpoint.status_code == 200
        assert endpoint.text == "OK"
