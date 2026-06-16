import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
@pytest.fixture(scope="function")
def lambdatest_driver():
    LT_USER = os.getenv("LT_USERNAME")
    LT_KEY = os.getenv("LT_ACCESS_KEY")
    lt_options = {
        "build": "Nightly Release v2.1",
        "name": "macOS Safari Validation",
        "platformName": "macOS Sonoma",
        "browserName": "Safari",
        "browserVersion": "17.0",
        "visual": True, # Capture Step-by-Step Screenshots
        "video": True,  # Record a Video of the Execution!
        "network": True # Capture Network Logs
    }
    options = ChromeOptions()
    options.set_capability('LT:Options', lt_options)
    remote_url = f"https://{LT_USER}:{LT_KEY}@hub.lambdatest.com/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver
    driver.execute_script("lambda-status=passed")
    driver.quit()