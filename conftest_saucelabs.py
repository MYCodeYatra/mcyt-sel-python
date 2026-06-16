import os
import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options as EdgeOptions
@pytest.fixture(scope="function")
def saucelabs_driver():
    SAUCE_USER = os.getenv("SAUCE_USERNAME")
    SAUCE_KEY = os.getenv("SAUCE_ACCESS_KEY")
    # Requesting Windows 11 with Microsoft Edge!
    sauce_options = {
        "build": "Nightly Release v2.1",
        "name": "Windows 11 Edge Validation",
        "screenResolution": "1920x1080"
    }
    options = EdgeOptions()
    options.browser_version = "latest"
    options.platform_name = "Windows 11"
    options.set_capability('sauce:options', sauce_options)
    # Sauce Labs Data Center URL (US-West in this example)
    remote_url = f"https://{SAUCE_USER}:{SAUCE_KEY}@ondemand.us-west-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver
    # Update Sauce Labs Status
    driver.execute_script("sauce:job-result=passed")
    driver.quit()