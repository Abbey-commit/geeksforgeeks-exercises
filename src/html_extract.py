from urllib.request import urlopen
from bs4 import BeautifulSoup, Tag

def get_page(url: str) -> BeautifulSoup:
    return BeautifulSoup(urlopen(url), "html.parser")

def find_table_caption(soup: BeautifulSoup, caption_text: str = "Anscombe's quartet") -> Tag:
    for table in soup.find_all('table'):
        if table.caption and table.caption.text.strip() == caption_text.strip():
            return table
    raise RuntimeError(f"<table> with caption {caption_text!r} not found")

def table_row_data_iter(table: Tag):
    for row in table.find_all('tr'):
        yield [cell.get_text(strip=True) for cell in row.find_all(['td', 'th'])]    
    