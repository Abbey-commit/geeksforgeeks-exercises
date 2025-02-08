import argparse
import csv
import json
from kaggle_client import RestAccess
from web_scraper import fetch_html, parse_html
from html_extract import get_page, find_table_caption, table_row_data_iter
from extract import Series1Pair, Series2Pair, Series3Pair, Series4Pair

def main():
    parser = argparse.ArgumentParser(description="Acquire and transform data.")
    parser.add_argument("-o,", "--output", required=True, help="Output directory")
    parser.add_argument("-k", "--kaggle", help="Path to Kaggle API key file")
    parser.add_argument("--zip", help="Kaggle dataset reference (ownerSlug/datasetSluug)")
    parser.add_argument("--search", help="Search term for Kaggle datasets")
    parser.add_argument("--scape", help="URL to scrape data from")
    parser.add_argument("--caption", help="Caption of the table to scrape")
    args = parser.parse_args()

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
    
    if args.scape and args.caption:
        soup = get_page(args.scape)
        table = find_table_caption(soup, args.caption)
        data = list(table_row_data_iter(table))
        output_path = os.path.join(args.output, "scrape_data.json")
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Data scraped and saved to {output_path}")

if __name__=="__main__":
    main()