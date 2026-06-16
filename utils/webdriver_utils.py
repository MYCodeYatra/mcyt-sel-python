from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
class WebDriverUtils:
    def __init__(self, driver, default_timeout=10):
        self.driver = driver
        self.timeout = default_timeout
    def wait_for_element_visible(self, locator):
        """Waits for an element to be visible on the DOM."""
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            return wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(f"Element {locator} not visible after {self.timeout}s")
    def click_element(self, locator):
        """Waits for an element to be clickable and clicks it, with JS fallback."""
        try:
            wait = WebDriverWait(self.driver, self.timeout)
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
            print(f"Successfully clicked element: {locator}")
        except ElementClickInterceptedException:
            print(f"Standard click failed for {locator}. Attempting JS Click...")
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)
    def enter_text(self, locator, text):
        """Clears the field and enters text safely."""
        element = self.wait_for_element_visible(locator)
        element.clear()
        element.send_keys(text)
        print(f"Entered text '{text}' into {locator}")