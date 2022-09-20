import unittest
from urllib import request
import app


class TestApp(unittest.TestCase):
    # name start with 'test_'
    MOCK_OBJ = [{
        "id": "1",
        "description": "Pumpkin",
        "amount" : 179000,
        "currency": "HUF",
        "spent_at": "2022-02-23T14:47:20.381Z"
    },]
    
    def test_get_spendings(self):
        API_URL = "http://localhost:3000/spendings"
        r = request.get(TestApp.API_URL)
        self.assertEqual(r.status_code,200)
        
        
if __name__ == '__main__':
    unittest.main()