import json
import pytest
from selenium import webdriver
# Pytest fixture that runs before every test
@pytest.fixture
def authenticated_driver():
    driver = webdriver.Chrome()
    # 1. Navigate to the domain (Required before injecting cookies!)
    driver.get("https://github.com")
    # 2. Load the cookies from our JSON file
    with open("auth_state.json", "r") as file:
        saved_cookies = json.load(file)
    # 3. Inject the cookies instantly
    for cookie in saved_cookies:
        driver.add_cookie(cookie)
    # 4. Refresh to apply the authentication state!
    driver.refresh()
    # Yield the fully logged-in driver to the test
    yield driver
    # Teardown
    driver.quit()
def test_dashboard_access(authenticated_driver):
    # This test starts ALREADY logged in!
    authenticated_driver.get("https://github.com/dashboard")
    print("\n[Test 1] Instantly accessed secure dashboard without logging in!")
    assert "dashboard" in authenticated_driver.current_url
def test_profile_access(authenticated_driver):
    # This test also starts ALREADY logged in!
    authenticated_driver.get("https://github.com/settings/profile")
    print("\n[Test 2] Instantly accessed secure profile without logging in!")
    assert "settings" in authenticated_driver.current_url