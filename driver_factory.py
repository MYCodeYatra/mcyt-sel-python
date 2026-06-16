from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome", headless=False):
        browser_name = browser_name.lower().strip()
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            driver = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            driver = webdriver.Firefox(options=options)
        elif browser_name == "edge":
            # Edge shares options with Chrome internally in many setups
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument("headless")
            driver = webdriver.Edge(options=options)
        else:
            raise ValueError(f"Browser '{browser_name}' is not supported by the factory!")
        # Global configurations applied to ALL browsers
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver