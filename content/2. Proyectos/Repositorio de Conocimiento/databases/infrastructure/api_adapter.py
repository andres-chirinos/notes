# infrastructure/api_adapter.py
import requests

class APIAdapter:
    def fetch_data(self, params):
        url = params["url"]
        headers = params.get("headers", {})
        response = requests.get(url, headers=headers)
        return response.json() if response.status_code == 200 else None
