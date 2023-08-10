
import requests

def Post_Json_data(data, url):
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

import unittest
from unittest.mock import patch, MagicMock, mock_open

class TestPostJsonData(unittest.TestCase):
    @patch('requests.post')
    def test_Post_Json_data(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_post.return_value = mock_response

        data = {"key": "value"}
        url = "http://example.com"

        response = Post_Json_data(data, url)
        self.assertEqual(response, 200)

if __name__ == '__main__':
    unittest.main()
