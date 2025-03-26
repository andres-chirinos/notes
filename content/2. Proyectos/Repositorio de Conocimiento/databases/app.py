# app.py
from core.services import DataExtractorService

extractor = DataExtractorService()

# Extraer datos de CKAN
ckan_data = extractor.extract_data("ckan", {"base_url": "https://datos.gob.bo","dataset_id": "poblacion-bolivia"})
print("CKAN Data:", ckan_data)

# Extraer datos desde una API
api_data = extractor.extract_data("api", {"url": "https://jsonplaceholder.typicode.com/posts"})
print("API Data:", api_data)

# Extraer datos por Web Scraping
web_data = extractor.extract_data("web", {"url": "https://example.com"})
print("Web Scraping Data:", web_data)

# Extraer datos de una Base de Datos
db_data = extractor.extract_data("db", {"db_path": "data.db", "query": "SELECT * FROM users"})
print("DB Data:", db_data)
