import pytest
from core.driver_factory import DriverFactory
from utils.logger import get_logger

logger = get_logger(__name__)

@pytest.fixture(scope="function")
def driver(request):
    logger.info("Initializing WebDriver...")
    browser = request.config.getoption("--browser", default="chrome")
    driver_instance = DriverFactory.get_driver(browser)
    
    yield driver_instance
    
    logger.info("Tearing down WebDriver...")
    if driver_instance:
        driver_instance.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
