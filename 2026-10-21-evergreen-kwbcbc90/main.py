"""Polite scraping: one session, a user-agent, a timeout, raise on errors, 1 second between requests."""

import sys
import time

from bs4 import BeautifulSoup

HEADERS = {"user-agent": "my-app/0.0.1"}
SAMPLE_HTML = '<article class="product_pod"><h3><a href="a.html">A</a></h3></article>' * 3


def count_books(html):
    return len(BeautifulSoup(html, "html.parser").select("article.product_pod h3 a"))


def crawl(pages=3):
    import requests

    with requests.Session() as s:
        for n in range(1, pages + 1):
            r = s.get(f"https://books.toscrape.com/catalogue/page-{n}.html", headers=HEADERS, timeout=10)
            r.raise_for_status()
            print(count_books(r.text))
            time.sleep(1)


if __name__ == "__main__":
    assert count_books(SAMPLE_HTML) == 3
    print("offline sample ok")
    if "--live" in sys.argv:
        crawl()
