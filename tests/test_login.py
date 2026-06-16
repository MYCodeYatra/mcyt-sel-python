import pytest
from selenium import webdriver
from pages.login_page import LoginPage
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
def test_successful_login(driver):
    # 1. Initialize the Page Object
    login_page = LoginPage(driver)
    # 2. Perform the high-level action
    login_page.login("admin", "password123")
    # 3. Assert the result (Assertions stay in the test file!)
    assert "Dashboard" in driver.title