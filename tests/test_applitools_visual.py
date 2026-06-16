import os
import pytest
from selenium import webdriver
from applitools.selenium import Eyes, Target
# Define our API Key from the Environment Variable
APPLITOOLS_API_KEY = os.getenv("APPLITOOLS_API_KEY", "YOUR_FREE_API_KEY")
@pytest.fixture(scope="function")
def eyes():
    """Setup Applitools Eyes as a Pytest Fixture"""
    eyes_instance = Eyes()
    eyes_instance.api_key = APPLITOOLS_API_KEY
    yield eyes_instance
    # After the test, ensure eyes are safely closed and test results are finalized
    eyes_instance.abort_if_not_closed()
def test_homepage_ai_visual_regression(eyes):
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 800)
    # 1. Start the Visual Test!
    # Parameters: (driver, App Name, Test Name)
    print("\n[Visual AI] Opening Applitools Eyes...")
    eyes.open(driver, "MyCodeYatra App", "Homepage Desktop View")
    # 2. Navigate the application
    driver.get("https://httpbin.org/")
    # 3. Capture the screen and send it to the Applitools AI Brain
    print("[Visual AI] Checking the main window...")
    eyes.check("Main Dashboard", Target.window().fully())
    # 4. Close the eyes and wait for the AI result!
    # If the AI detects a regression, eyes.close() will throw a DiffsFoundError
    print("[Visual AI] Closing eyes and waiting for cloud analysis...")
    result = eyes.close(raise_ex=True)
    print(f"✅ Applitools Test Passed! View dashboard: {result.url}")
    driver.quit()