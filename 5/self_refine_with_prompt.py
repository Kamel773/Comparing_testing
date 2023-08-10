import requests
from requests.exceptions import RequestException

def uploading(file_path, url):
    try:
        with open(file_path, 'rb') as file:
            response = requests.post(url, files={'file': file})
        return response
    except (FileNotFoundError, IsADirectoryError):
        raise ValueError("Invalid file path!")
    except RequestException:
        raise ValueError("Error occurred during file upload!")