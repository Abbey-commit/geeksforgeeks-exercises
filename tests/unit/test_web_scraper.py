import unittest
from unittest.mock import patch, MagicMock
from web_scraper import fatch_html, parse_html

class TestWebScrapper(unittest.TestCase):

    @patch("requests.get")
    def test_fetch_html(self, mock_get):
        mock_get.return_value.text = "<html></html>"
        html_content = fetch_html("http://example.com")
        self.assertEqual(html_content, "<html></html>")

    @patch("web_scrapper.BeautifulSoup")
    def test_parse_html(self, mock_soup):
        mock_soup.return_value = "parsed data"
        html_content = "<html></html>"
        parsed_data = parse_html(html_content)
        self.assertEqual(parsed_data, "parsed data")

if __name__ == '__main__':
    unittest.main()