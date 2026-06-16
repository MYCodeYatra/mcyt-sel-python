import pytest
from selenium import webdriver
# 1. Define custom CLI options for our plugin
def pytest_addoption(parser):
    parser.addoption(
        "--mycodeyatra-browser", 
        action="store", 
        default="chrome", 
        help="Browser to run tests on via mycodeyatra plugin"
    )
# 2. Define the globally available fixture
@pytest.fixture
def driver(request):
    """
    Provides a configured Selenium WebDriver instance.
    This will become available to EVERY project that installs this plugin!
    """
    browser = request.config.getoption("--mycodeyatra-browser").lower()
    print(f"\n[Plugin] Initializing {browser} driver...")
    if browser == "chrome":
        driver_instance = webdriver.Chrome()
    elif browser == "firefox":
        driver_instance = webdriver.Firefox()
    else:
        raise ValueError("Unsupported browser")
    driver_instance.maximize_window()
    yield driver_instance
    print(f"\n[Plugin] Tearing down {browser} driver...")
    driver_instance.quit()