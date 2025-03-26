# infrastructure/ckan_adapter.py
import requests

class CKANAdapter:
    def fetch_data(self, params):
        base_url = params.get("base_url")
        dataset_id = params["dataset_id"]
        url = f"{base_url}/api/3/action/package_show?id={dataset_id}"
        response = requests.get(url)
        return response.json() if response.status_code == 200 else None
