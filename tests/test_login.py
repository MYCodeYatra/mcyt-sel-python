import pytest
from pages.login_page import LoginPage
from core.config_manager import ConfigManager

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_successful_login(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login(ConfigManager.ADMIN_USER, ConfigManager.ADMIN_PASS)
        
        # Simple assertion for now
        assert "dashboard" in driver.current_url.lower()

    def test_invalid_login(self, driver):
        login_page = LoginPage(driver)
        login_page.navigate()
        login_page.login("wronguser", "wrongpass")
        
        assert login_page.is_visible(login_page.ERROR_MESSAGE)
