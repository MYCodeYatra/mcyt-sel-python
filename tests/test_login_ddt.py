import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
# Our list of Test Data
login_data = [
    ("admin", "Pass123", "Dashboard"),
    ("admin", "wrong", "Invalid credentials"),
    ("baduser", "Pass123", "Invalid credentials"),
    ("", "", "Username required")
]
@pytest.mark.parametrize("username, password, expected_message", login_data)
def test_login_scenarios(username, password, expected_message):
    driver = webdriver.Chrome()
    driver.get("https://mycodeyatra.com/login")
    driver.find_element(By.ID, "user").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    driver.find_element(By.ID, "login-btn").click()
    body_text = driver.find_element(By.TAG_NAME, "body").text
    assert expected_message in body_text
    driver.quit()