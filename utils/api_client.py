import requests
from core.config_manager import ConfigManager

class APIClient:
    @staticmethod
    def get_auth_token(username, password):
        url = f"{ConfigManager.BASE_URL}/api/auth"
        response = requests.post(url, json={"username": username, "password": password})
        if response.status_code == 200:
            return response.json().get("token")
        raise Exception("Failed to fetch API token")
