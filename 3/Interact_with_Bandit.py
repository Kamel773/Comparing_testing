
import requests

def Post_Json_data(data, url):
    headers = {'Content-type': 'application/json'}
    response = requests.post(url, json=data, headers=headers, timeout=10)
    return response.status_code
