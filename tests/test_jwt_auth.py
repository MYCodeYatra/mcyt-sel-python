import pytest
import requests
from selenium import webdriver
def get_jwt_via_api():
    """Logs in via API and returns the JWT Bearer token."""
    payload = {"username": "admin", "password": "SuperSecretPassword!"}
    response = requests.post("https://api.mycodeyatra.com/v1/login", json=payload)
    return response.json().get("access_token")
def test_dashboard_with_jwt_injection():
    # 1. Fetch the JWT via API
    jwt_token = get_jwt_via_api()
    driver = webdriver.Chrome()
    # 2. Navigate to the domain so LocalStorage is initialized for that origin
    driver.get("https://mycodeyatra.com")
    # 3. Inject the JWT into LocalStorage using JavaScript!
    # Note: You must know the EXACT key your React app expects (e.g., 'authToken')
    js_command = f"window.localStorage.setItem('authToken', '{jwt_token}');"
    driver.execute_script(js_command)
    # 4. Refresh or Navigate to the protected route
    driver.get("https://mycodeyatra.com/dashboard")
    # The React app will read the token from LocalStorage and grant access instantly!
    assert "Secure Data" in driver.page_source
    driver.quit()