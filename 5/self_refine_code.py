
import requests

def uploading(file_path, url):
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': file})
    return response
