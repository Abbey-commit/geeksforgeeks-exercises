# Design Document

## Overview 
This document outlines the design of the Data Acquisition project, which involves acquiring data from various sources including CSV files, web APIs, and web scraping.

## Project Structure
The project consists of three main phrases:
1. **Project 1.1: Data Acquisition Base Application** Found in folder project_0.
    - Acquires data from CSV file and transforms it into JSON format.
2. **Project 1.2: Acquire Data from a Web Service**
    - Integrates with the Kaggle API to download datasets.
3. **Project 1.3: Scrape Data from a Web Page**
    - Scrape data from HTML tables on a web page.

## Components

### CSV Extraction
- **Module**: `src/extract.py`
- **Classes**:
  - `PairBuilder`: Abstract base class for converting CSV rows to `XYPair` objects.
  - `Series1Pair`, `Series2Pair`, `Series3Pair`, `Series4Pair`: Concrete implemetation of `PairBuilder` 

### Kaggle API Integration
- **Module**: `src/kaggle_client.py`
- **Class**: `ResrAccess`
  - `get_page(url: str) -> BeautifulSoup`: Fetches and parses an HTML page.
  - `find_table_caption(soup: BeautifulSoup, caption_text: str) -> Tag`: Find a table with specific caption.
  - `table_row_data_iter(table: Tag)`: Iterates over rows in the table.

## CLI Application
- **Module**: `src/acquire.py`
- **Function**: `main()`
  - Parses command-line arguments.
  - Invokes appropriate data acquisition methods based on the arguments.

## Testing
- **Unit Test**: Locate in `tests/unit`
  - Test individual modules and functions.
- **Acceptance Tests**: Located in `tests/features/` and `tests/steps/`
  - Use `behave` to define and run feature-based tests.

## Dependencies
- `requests`: For making HTTP requests.
- `beautifulsoup4`: For parsing HTML.
- `pytest`: For unit testing.
- `behave`: For acceptance testing.

## Architecture Diagrams
### Component Diagram
![Component Diagram](component_diagram.png)

### Context Diagram

## Security Considerations
- API keys (e.g., `kaggle.json`) should be kept secure and not included in version control.
- Sensitive information should be handled carefully and stored in a secured manner.

## Future Enhancements
- Support additional data formats (e.g., JSON).
- Implemen more robust error handling and logging.
- Extend the CLI to support more flexible query parameters.