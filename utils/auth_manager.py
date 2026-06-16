import json
from selenium import webdriver
from selenium.webdriver.common.by import By
def generate_global_auth_state():
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    # 1. Execute the slow UI Login exactly once
    print("\n[Auth] Executing one-time UI login...")
    driver.find_element(By.ID, "login_field").send_keys("test_automation_user")
    driver.find_element(By.ID, "password").send_keys("SecurePassword123!")
    driver.find_element(By.NAME, "commit").click()
    # 2. Extract the authenticated cookies
    cookies = driver.get_cookies()
    # 3. Save the cookies to a JSON file on the hard drive
    with open("auth_state.json", "w") as file:
        json.dump(cookies, file)
    print(f"[Auth] Saved {len(cookies)} cookies to auth_state.json!")
    driver.quit()
if __name__ == "__main__":
    generate_global_auth_state()