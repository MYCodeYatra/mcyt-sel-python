from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

class DriverFactory:
    @staticmethod
    def get_driver(browser_name="chrome"):
        browser_name = browser_name.lower()
        if browser_name == "chrome":
            options = ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            # options.add_argument("--headless=new")
            return webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            return webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")
