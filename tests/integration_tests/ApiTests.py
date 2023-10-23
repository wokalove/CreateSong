import requests
from flask import Flask
import unittest
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from api.ApiToTests import configure_routes

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_connection(self):
        configure_routes(self.app)
        client = self.app.test_client()
        url = '/user/create-song'

        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        
    
    # def test_received_data(self, response):
    #     response_data = isinstance(response.get_data(),(bytes, bytearray))
    #     self.assertTrue(response_data)

if __name__=="__main__":
    unittest.main()        


# https://www.youtube.com/watch?v=sL_PWBOABWo