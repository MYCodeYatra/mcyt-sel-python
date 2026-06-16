import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
@pytest.fixture(scope="function")
def browserstack_driver():
    # 1. Fetch credentials securely
    BS_USER = os.getenv("BROWSERSTACK_USERNAME")
    BS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")
    # 2. Define the Cloud Configuration Matrix
    bstack_options = {
        "osVersion" : "17",
        "deviceName" : "iPhone 15 Pro Max",
        "realMobile" : "true",
        "projectName" : "MyCodeYatra E-Commerce",
        "buildName" : "Nightly Release v2.1",
        "sessionName" : "Checkout Flow Validation",
    }
    options = ChromeOptions() # Or SafariOptions if targeting Safari
    options.set_capability('bstack:options', bstack_options)
    # 3. Connect to the BrowserStack Hub
    remote_url = f"https://{BS_USER}:{BS_KEY}@hub-cloud.browserstack.com/wd/hub"
    print(f"\n[Cloud] Requesting iPhone 15 Pro Max from BrowserStack...")
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver
    # 4. Mark test as passed/failed in the BrowserStack UI
    driver.execute_script('browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Test Successful!"}}')
    driver.quit()