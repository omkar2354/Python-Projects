📚 Books Web Scraper (Python Project)

A complete Python web-scraping project that extracts book details from BooksToScrape.com using Requests, BeautifulSoup, and CSV export.
The scraper is designed to be fast, reliable, and structured, with retry logic, delays, page navigation, and detailed product extraction.

🚀 Project Overview

This project scrapes all books from the website:

🔹 Title
🔹 Price
🔹 Availability
🔹 Rating (1–5)
🔹 UPC
🔹 Product description
🔹 Category
🔹 Product page URL
🔹 Image URL
🔹 Timestamp (scraped_at)

All scraped data is saved into a structured CSV file inside the output/ folder.

🧠 Features
✔ 1. Page-by-page scraping

The scraper automatically moves through all pages using the “Next” pagination.

✔ 2. Product-level deep scraping

Each book’s product page is opened and details like UPC, description, category, and image URL are extracted.

✔ 3. Anti-blocking behaviour

Random delays between requests

Custom User-Agent

Automatic retries on timeouts

✔ 4. Progress Bar

Uses tqdm to show real-time scraping progress.

✔ 5. Clean CSV Output

All fields are stored in:

output/books.csv

🛠️ Technologies Used

Python 3

requests

BeautifulSoup4

tqdm

csv

urllib

dateutil

os

random

📦 Project Structure
Book-Scraper/
│
├── scrape_books.py        # Main scraping script
├── output/
│   └── books.csv          # Scraped data (auto-generated)
└── README.md

🔧 How to Run the Scraper
1️⃣ Install dependencies
pip install requests beautifulsoup4 python-dateutil tqdm

2️⃣ Run the script
python scrape_books.py

3️⃣ After completion

Your extracted data will appear here:

output/books.csv

📁 CSV Output Fields
Field	Description
title	Book name
price	Price of the book
availability	In stock / Out of stock
rating	Star rating (1–5)
product_page_url	Direct link to product
upc	Product UPC code
desc	Book description
category	Genre/category
img_url	Cover image URL
scraped_at	Local timestamp
🔍 How the Script Works (Short Summary)

Sends GET request to each page

Parses books listed

Extracts basic details

Opens each book’s detail page

Extracts deep metadata

Writes everything to CSV

Moves to the next page until no pages remain

The scraper includes robust error handling and retry logic to avoid failures.

🏁 Final Output

You get a high-quality CSV dataset with all books from the website — perfect for:

✔ Data analysis
✔ Machine learning
✔ Portfolio projects
✔ Practice datasets
✔ ETL tasks
