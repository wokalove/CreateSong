import requests
from flask import Flask

import unittest


app = Flask(__name__)

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    # def test_route(self):
    #     response = self.app.get('/user/create-song')
    #     self.assertEqual(response.status_code, 200)

    def test_passed_data(self):
        response = self.app.get('/user/create-song')
        response_data = isinstance(response.get_data(),(bytes, bytearray))

        assert 'File is binary'

    


if __name__=="__main__":
    unittest.main()        
