import pytest
from selenium import webdriver
from actor import Actor, BrowseTheWeb
from tasks import LoginTask
from questions import TextOf
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://mycodeyatra.com/login")
    yield driver
    driver.quit()
def test_screenplay_login(driver):
    # 1. Define the Actor and give them the Ability to use Selenium
    james = Actor("James").can(BrowseTheWeb(driver))
    # 2. The Actor attempts a high-level Task
    james.attempts_to(
        LoginTask("admin", "secure_password")
    )
    # 3. The Actor asks a Question to verify the outcome
    WELCOME_MSG = ("id", "toast")
    assert james.asks(TextOf(WELCOME_MSG)) == "Welcome back, James!"