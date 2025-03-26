# core/services.py
from infrastructure.ckan_adapter import CKANAdapter
from infrastructure.api_adapter import APIAdapter
from infrastructure.web_scraper import WebScraper
from infrastructure.db_adapter import DBAdapter

class DataExtractorService:
    def __init__(self):
        self.sources = {
            "ckan": CKANAdapter(),
            "api": APIAdapter(),
            "web": WebScraper(),
            "db": DBAdapter()
        }

    def extract_data(self, source_type, params):
        if source_type not in self.sources:
            raise ValueError(f"Fuente {source_type} no soportada")
        return self.sources[source_type].fetch_data(params)
