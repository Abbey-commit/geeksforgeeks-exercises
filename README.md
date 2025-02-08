# Data Acquisition Project
This project demonstrate data acquisition from various sources including CSV file web APIs, and  and web scraping.

## Projects

Project 1.1: Data  Acquisition Base Application
    . Acquires data from CSV file and transform it into JSON format for easy readability.
Project 1.2: Acquire Data from a Web Service
    . Integrate with the Kaggle API to download datasets.
Project 1.3: Scrape Data from a Web Page
    . Scrape Data from HTML tables on a web page.

Usage

Run the following Command for versions

For the API Integration Application (Project 1.2):
```sh
poetry run python src/acquire.py -o output_directory --page https://kaggle.com/kaggle.json/
```

For the webscrping run (Project 1.3):
```sh
poetry run python src/acquire.py -o output_directory --page 'https://wikipedia.com' c Example caption
```


Install dependdencies using Poetry:
```sh
poetry install
```

## Usage
To run the application, use the following command:
```sh
poetry run python src/acquire.py -o output_directory data/Ascombe_quartet_data.csv