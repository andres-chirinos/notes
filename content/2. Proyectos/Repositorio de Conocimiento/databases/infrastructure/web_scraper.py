# infrastructure/web_scraper.py
import requests
from bs4 import BeautifulSoup

class WebScraper:
    def fetch_data(self, params):
        url = params["url"]
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            return {"title": soup.title.string, "content": soup.get_text()}
        return None
