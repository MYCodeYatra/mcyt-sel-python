import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.healing_driver import SelfHealingDriver
def test_login_with_self_healing():
    # Initialize standard Chrome
    raw_driver = webdriver.Chrome()
    # Wrap it in our AI Engine!
    driver = SelfHealingDriver(raw_driver)
    driver.get("https://mycodeyatra.com/login")
    # Enter credentials
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("Pass123")
    # ⚠️ THE BROKEN LOCATOR!
    # Let's pretend the original ID was "submit-btn", 
    # but the dev changed it to "login-primary-button" this morning!
    # The standard driver would crash here. 
    # Our engine will catch the exception, analyze the DOM, find the 
    # new "login-primary-button", and click it automatically!
    driver.find_element(By.ID, "submit-btn").click()
    # Verify success
    assert "dashboard" in raw_driver.current_url
    raw_driver.quit()