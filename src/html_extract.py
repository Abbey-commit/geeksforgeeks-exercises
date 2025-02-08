from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def get_page(url: str) -> BeautifulSoup:
    return BeautifulSoup(urlopen(url), "html.parser")

def find_tables(soup: BeautifulSoup) -> list[Tag]:
    tables = soup.find_all('table')
    if not tables:
        raise RuntimeError("No tables found on the page")
    return tables

def table_row_data_iter(table: Tag):
    for row in table.find_all('tr'):
        yield [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]