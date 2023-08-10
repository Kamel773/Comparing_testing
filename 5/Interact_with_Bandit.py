
import requests

def uploading(file_path, url):
    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': file}, timeout=10)
    return response

# Example usage:
# response = uploading('test_file.txt', 'http://testurl.com')
# print(response.status_code)
