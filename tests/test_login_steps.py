from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 1. Load the feature file!
scenarios('../features/login.feature')
# 2. Step Definitions
@given('the user navigates to the login page')
def navigate_to_login(driver):
    driver.get("https://mycodeyatra.com/login")
# We use "parsers.parse" to capture the string "admin" from the Gherkin step!
@when(parsers.parse('the user enters the username "{username}"'))
def enter_username(driver, username):
    driver.find_element(By.ID, "username").send_keys(username)
@when(parsers.parse('the user enters the password "{password}"'))
def enter_password(driver, password):
    driver.find_element(By.ID, "password").send_keys(password)
@when('the user clicks the login button')
def click_login(driver):
    driver.find_element(By.ID, "login-btn").click()
@then('the user should be redirected to the dashboard')
def verify_dashboard_redirect(driver):
    # Wait for the URL to change to the dashboard
    WebDriverWait(driver, 10).until(
        EC.url_contains("/dashboard")
    )
    assert "dashboard" in driver.current_url.lower()