import unittest
from unittest.mock import MagicMock, patch
from app import get_spendings


class TestGetSpendings(unittest.TestCase):

    @patch('app.request')
    def test_get_spendings(self, mock_get_spendings):
        
        # mock_results = MagicMock()
        mock_get_spendings.return_value.json.return_value = {"data":[
        {
        "amount": 1500000,
        "currency": "HUF",
        "description": "Bérlet",
        "id": 17,
        "spent_at": "2022-09-21T13:24:20"
    }]}
        mock_get_spendings.get.return_value = mock_get_spendings
        self.assertEqual(get_spendings(), mock_get_spendings.json()['data'][0]['description'],'Coffee')
        
    
    @patch('app.request')
    def test_fail_get_spendings(self, mock_request):
        
        mock_results = MagicMock(status_code=400)
        mock_results.json.return_value = {"data":[
        {
        "amount": 1500000,
        "currency": "HUF",
        "description": "Bérlet",
        "id": 17,
        "spent_at": "2022-09-21T13:24:20"
    }]}
        mock_request.get.return_value = mock_results
        self.assertEqual(get_spendings(), "Not accepted form!")
        
        
if __name__ == '__main__':
    unittest.main()