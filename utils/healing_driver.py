from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from utils.ai_healer import heal_locator
class SelfHealingDriver:
    def __init__(self, driver):
        self.driver = driver
    def get(self, url):
        self.driver.get(url)
    def find_element(self, by, value):
        try:
            # Step 1: Try the standard, original locator
            return self.driver.find_element(by, value)
        except NoSuchElementException:
            print(f"\n[Warning] Element not found: {value}. Engaging AI Healer...")
            # Step 2: Grab the DOM
            dom = self.driver.page_source
            # Step 3: Ask AI for the new locator
            new_css_selector = heal_locator(broken_locator=value, page_source=dom)
            # Step 4: Retry the find with the NEW locator!
            return self.driver.find_element(By.CSS_SELECTOR, new_css_selector)