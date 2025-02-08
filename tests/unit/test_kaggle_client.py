import unittest
from unittest.mock import patch, mock_open, MagicMock
import os
credentials_path = os.path.expanduser("/.Kaggle/kaggle.json")
from kaggle_client import RestAccess

class TestKaggleClient(unittest.TestCase):

    @patch("buitins.open", new_callable=mock_open, read_data='{"username":"test","key":testkey"}')
    def test_authenticate_kaggle(self, mock_file):
        api_key = RestAccess("/.Kaggle/kaggle.json")
        self.assertEqual(api_key.auth.username, "test")
        self.assertEqual(api_key.auth.password, "testkey")

    @patch("requests.get")
    def test_search_datasets(self, mock_get):
        mock_get.return_value.json = MagicMock(return_value={'datasets': []})
        api_key = RestAccess({"username": "test", "key": "test_key"})
        datasets = list(api_key.dataset_iter({"search": "test_search"}))
        self.assertEqual(datasets, [])


    @patch('requests.get')
    def test_download_dataset(self, mock_get):
        mock_get.return_value.iter_content = MagicMock(return_value=[b"testdata"])
        api_key = RestAccess({"username": "test", "key": "testkey"})
        zip_path = api_key.get_zip("owner", "dataset", "/temp")
        self.assertEqual(os.path.exists(zip_path))

if __name__ == "__main__":
    unittest.main()