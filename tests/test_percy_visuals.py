import os
import pytest
from selenium import webdriver
from percy import percy_snapshot
@pytest.fixture(scope="function")
def driver():
    # Setup Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver_instance = webdriver.Chrome(options=options)
    yield driver_instance
    driver_instance.quit()
def test_homepage_percy_snapshot(driver):
    # 1. Navigate to the application normally
    print("\n[Selenium] Navigating to the target application...")
    driver.get("https://httpbin.org/")
    # 2. Capture the DOM Snapshot!
    # Percy does NOT take a screenshot here. It captures the raw HTML/CSS!
    print("[Percy] Capturing DOM state and sending to BrowserStack Cloud...")
    percy_snapshot(driver, "Homepage Visual Baseline")
    print("✅ Snapshot captured! Review the visual diffs in the Percy Dashboard.")