from utils.webdriver_utils import WebDriverUtils
# Every Page Object will inherit from this BasePage
class BasePage(WebDriverUtils):
    def __init__(self, driver):
        # Pass the driver up to the Utility class!
        super().__init__(driver)