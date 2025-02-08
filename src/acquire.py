import argparse
import csv
import os
import json
from html_extract import get_page, find_tables, table_row_data_iter
from kaggle_client import RestAccess
from web_scraper import fetch_html, parse_html
from extract import Series1Pair, Series2Pair, Series3Pair, Series4Pair

def save_as_json(data, output_path):
    with open(output_path, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Data saved to {output_path}")

def save_as_csv(data, output_path):
    with open(output_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    print(f"Data saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Acquire and transform data.")
    parser.add_argument("-o,", "--output", required=True, help="Output directory")
    parser.add_argument("-k", "--kaggle", help="Path to Kaggle API key file")
    parser.add_argument("--zip", help="Kaggle dataset reference (ownerSlug/datasetSluug)")
    parser.add_argument("--search", help="Search term for Kaggle datasets")
    parser.add_argument("--scrape", help="URL to scrape data from")
    parser.add_argument("--caption", help="Caption of the table to scrape")
    parser.add_argument("--format", choices=['json', 'csv'], default='json', help="Output format (json or csv)")
    args = parser.parse_args()

    if args.scrape:
        soup = get_page(args.scrape)
        tables = find_tables(soup)
        print(f"Number of tables found: {len(tables)}")
        for idx, table in enumerate(tables):
            data = list(table_row_data_iter(table))
            output_filename = f"scraped_data_table_{idx + 1}.{args.format}"
            output_path = os.path.join(args.output, output_filename)
            if args.format == 'json':
                save_as_json(data, output_path)
            elif args.format == 'csv':
                save_as_csv(data, output_path)

    if args.kaggle:
        api_key = RestAccess(args.kaggle)
        if args.search:
            datasets = api_key.dataset_iter({"search": args.search})
            for dataset in datasets:
                print(dataset)
        if args.zip:
            owner_slug, dataset_slug = args.zip.split('/')
            zip_path = api_key.get_zip(owner_slug, dataset_slug, args.output)
            print(f"Dataset download to {zip_path}")

    if args.scrape:
        soup = get_page(args.scrape)
        tables = find_tables(soup)
        print(f"Number of tables found: {len(tables)}")
        for idx, table in enumerate(tables):
            print(f"Table {idx + 1} contents:")
            for row in table_row_data_iter(table):
                print(row)   

if __name__=="__main__":
    main()