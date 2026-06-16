import pytest
import requests
from selenium import webdriver
def get_session_cookie_via_api():
    """Logs in via API and returns the session cookie value in 100ms."""
    payload = {"username": "admin", "password": "SuperSecretPassword!"}
    response = requests.post("https://api.mycodeyatra.com/v1/auth", json=payload)
    return response.cookies.get("session_id")
def test_dashboard_with_cookie_injection():
    # 1. Get the token instantly via API
    session_token = get_session_cookie_via_api()
    driver = webdriver.Chrome()
    # 2. Navigate to the domain (We just hit the homepage, NOT the login page)
    driver.get("https://mycodeyatra.com")
    # 3. Inject the Cookie
    cookie_dict = {
        'name': 'session_id',
        'value': session_token,
        'domain': 'mycodeyatra.com',
        'path': '/',
        'secure': True
    }
    driver.add_cookie(cookie_dict)
    # 4. Navigate directly to the protected Dashboard!
    driver.get("https://mycodeyatra.com/dashboard")
    # Assert we are logged in without ever seeing the Login UI
    assert "Welcome back, Admin" in driver.page_source
    driver.quit()