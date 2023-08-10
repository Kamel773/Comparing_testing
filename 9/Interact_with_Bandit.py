
import requests

def append_data_from_url(url, file_name):
    response = requests.get(url, timeout=10)
    with open(file_name, 'a') as f:
        f.write(response.content.decode())
