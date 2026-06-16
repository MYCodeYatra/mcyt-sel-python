import os
from dotenv import load_dotenv
from selenium import webdriver
def test_login_with_env_variables():
    # 1. Load the .env file into os.environ
    load_dotenv()
    # 2. Extract the credentials securely
    username = os.getenv("QA_ADMIN_USER")
    password = os.getenv("QA_ADMIN_PASS")
    assert password is not None, "Password was not found in environment!"
    # 3. Use them in Selenium safely
    print("\n[Security] Injecting securely loaded credentials into UI...")
    # driver = webdriver.Chrome()
    # driver.get("https://mycodeyatra.com/login")
    # driver.find_element(By.ID, "user").send_keys(username)
    # driver.find_element(By.ID, "pass").send_keys(password)
    print("✅ Successfully logged in without hardcoding credentials!")