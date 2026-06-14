from selenium.webdriver.common.by import By
from core.base_page import BasePage
from core.config_manager import ConfigManager

class LoginPage(BasePage):
    # Locators (Using CSS Selectors)
    USERNAME_INPUT = (By.CSS_SELECTOR, "#user")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#pass")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "#submit")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-msg")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = f"{ConfigManager.BASE_URL}/login"

    def navigate(self):
        self.open(self.url)

    def login(self, username, password):
        self.type_text(self.USERNAME_INPUT, username)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        
    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
