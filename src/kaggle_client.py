import json
import os
import requests
from pathlib import Path
from requests.auth import HTTPBasicAuth

class RestAccess:
    def __init__(self, credentials_path=None):
        # Determine the default credentials path
        default_kaggle_dir = os.getenv("KAGGLE_CONFIG_DIR")
        
        if credentials_path is None:
            # If KAGGLE_CONFIG_DIR is set, use it
            if default_kaggle_dir:
                credentials_path = os.path.join(default_kaggle_dir, "kaggle.json")
            else:
                # Use the standard location in the user's home directory
                credentials_path = os.path.expanduser("~/.kaggle/kaggle.json")
                
        # Normalize the path
        credentials_path = os.path.normpath(credentials_path)
        
        # Open and read the credentials file
        with open(credentials_path, 'r') as file:
            credentials = json.load(file)
            
        self.auth = HTTPBasicAuth(credentials['username'], credentials['key'])

    def get_zip(self, owner_slug, dataset_slug, output_dir):
        url = f"https://www.kaggle.com/api/v1/datasets/download/{owner_slug}/{dataset_slug}"
        response = requests.get(url, auth=self.auth, stream=True)
        zip_path = Path(output_dir) / f"{dataset_slug}.zip"
        with open(zip_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=128):
                file.write(chunk)
        return zip_path

    def dataset_iter(self, query):
        url = "https://www.kaggle.com/api/v1/datasets/list"
        page = 1
        while True:
            response = requests.get(url, params={**query, "page": str(page)}, auth=self.auth)
            if response.status_code == 200:
                details = response.json()
                if details:
                    yield from iter(details)
                    page += 1
                else:
                    break
            elif response.status_code == 429:
                retry_after = int(response.headers.get('Retry-After', 1))
                time.sleep(retry_after)
            else:
                break