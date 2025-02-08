import unittest
from unittest.mock import patch, MagicMock
from html_extract import get_page, find_table_caption, table_row_data_iter
from bs4 import BeautifulSoup

class TestHTMLExtract(unittest.TestCase):

    @patch("html_extract.ulropen")
    def test_get_page(self, mock_urlopen):
        mock_urlopen.return_value.read.value = "<html></html>"
        soup = get_page("http://example.com")
        self.assertIsInstance(soup, BeautifulSoup)

    def test_find_table_caption(self):
        html ="""
        <>html
        <body>
        <table>
            <caption>Anscombe's quartet</caption>
            <tr><td>10.0</td><td>8.04</td></tr>
        </table>
        </body>
        </html>
        """

        soup = BeautifulSoup(html, "html.parser")
        table = find_table_caption(soup, "Anscombe's quartet")
        self.assertIsNotNone(table)

    def test_row_data_iter(self):
        html = """"
        <table>
            <tr><td>10.0</td><td>8.04</td></tr>
            <tr><td>8.0</td><td>6.95</td></tr>
        </table>
        """
        soup = BeautifulSoup(html, "html.parser")
        table = soup.find('table')
        rows = list(table_row_data_iter('table'))
        self.assertEqual(rows, [['10.0', '8.04'], ['8.0', '6.95']])

if __name__ == "__main__":
    unittest.main()