import requests
from bs4 import BeautifulSoup
import csv
import time
from urllib.parse import urljoin
from datetime import datetime
from dateutil import tz
from tqdm import tqdm
import random
import os

BASE_URL = "http://books.toscrape.com/"
HEADERS = {"User-Agent": "books-scraper-bot/1.0"}
CSV_PATH = "output/books.csv"
DELAY_MIN, DELAY_MAX = 0.8, 1.6

def get_soup(url, retries=3):
    """Fetch a page and return a BeautifulSoup object, retrying on timeout."""
    for attempt in range(retries):
        try:
            r = requests.get(url, headers=HEADERS, timeout=25)
            r.raise_for_status()
            return BeautifulSoup(r.text, "html.parser")
        except requests.exceptions.Timeout:
            print(f"⚠️ Timeout on {url}, retrying ({attempt+1}/{retries})...")
            time.sleep(3)
        except requests.exceptions.RequestException as e:
            print(f"❌ Failed to fetch {url}: {e}")
            break
    return BeautifulSoup("", "html.parser")


def parse_rating(element):
    mapping = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    for cls in element.get("class", []):
        if cls in mapping:
            return mapping[cls]
    return None

def parse_product_page(product_url):
    soup = get_soup(product_url)
    table = soup.find("table", class_="table table-striped")
    upc = None
    if table:
        for row in table.find_all("tr"):
            if row.th.get_text(strip=True) == "UPC":
                upc = row.td.get_text(strip=True)

    desc = soup.find("div", id="product_description")
    desc_text = ""
    if desc:
        p = desc.find_next_sibling("p")
        if p:
            desc_text = p.get_text(strip=True)

    category = ""
    breadcrumb = soup.select("ul.breadcrumb li a")
    if len(breadcrumb) >= 3:
        category = breadcrumb[2].get_text(strip=True)

    img_tag = soup.select_one("div.item.active img")
    img_url = urljoin(product_url, img_tag["src"]) if img_tag else ""

    return {"upc": upc, "desc": desc_text, "category": category, "img_url": img_url}

def scrape():
    os.makedirs("output", exist_ok=True)
    csv_file = open(CSV_PATH, "w", newline="", encoding="utf-8")
    writer = csv.DictWriter(csv_file, fieldnames=[
        "title", "price", "availability", "rating", "product_page_url",
        "upc", "desc", "category", "img_url", "scraped_at"
    ])
    writer.writeheader()

    next_page = urljoin(BASE_URL, "index.html")
    pbar = tqdm(desc="Scraping pages")
    while next_page:
        soup = get_soup(next_page)
        products = soup.select("article.product_pod")
        for p in products:
            title = p.h3.a["title"]
            rel_url = p.h3.a["href"]
            product_page = urljoin(next_page, rel_url)
            price = p.select_one("p.price_color").get_text(strip=True)
            avail = p.select_one("p.instock.availability").get_text(strip=True)
            rating = parse_rating(p.find("p", class_="star-rating"))
            time.sleep(random.uniform(DELAY_MIN, DELAY_MAX))
            prod_data = parse_product_page(product_page)
            writer.writerow({
                "title": title,
                "price": price,
                "availability": avail,
                "rating": rating,
                "product_page_url": product_page,
                "upc": prod_data["upc"],
                "desc": prod_data["desc"],
                "category": prod_data["category"],
                "img_url": prod_data["img_url"],
                "scraped_at": datetime.now(tz=tz.tzlocal()).isoformat()
            })
        csv_file.flush()
        next_tag = soup.select_one("li.next a")
        next_page = urljoin(next_page, next_tag["href"]) if next_tag else None
        pbar.update(1)
    pbar.close()
    csv_file.close()
    print(f"✅ Done! Data saved to {CSV_PATH}")

if __name__ == "__main__":
    scrape()
