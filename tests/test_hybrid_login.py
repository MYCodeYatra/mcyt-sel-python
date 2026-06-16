import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def get_api_auth_cookie():
    """Step 1: Authenticate via API and extract the cookie"""
    login_url = "https://httpbin.org/cookies/set?session_token=secure_hybrid_token_123"
    # Hit the endpoint to generate a cookie
    response = requests.get(login_url)
    # Extract the cookie from the response
    cookie_value = response.cookies.get("session_token")
    print(f"\n[API] Successfully retrieved secure cookie: {cookie_value}")
    return cookie_value
def test_bypass_ui_login():
    """Step 2: Inject the API cookie into Selenium WebDriver"""
    # 1. Fetch the cookie using our API method (Takes < 0.1 seconds!)
    auth_cookie = get_api_auth_cookie()
    # 2. Launch Selenium
    driver = webdriver.Chrome()
    driver.maximize_window()
    # 3. Navigate to the domain first (You cannot set a cookie for a domain you aren't on)
    print("[UI] Navigating to domain...")
    driver.get("https://httpbin.org/")
    # 4. Inject the Cookie into the Browser!
    print("[UI] Injecting API cookie into the browser...")
    driver.add_cookie({
        "name": "session_token",
        "value": auth_cookie,
        "domain": "httpbin.org"
    })
    # 5. Navigate to the secure dashboard (Bypassing the login screen!)
    print("[UI] Navigating directly to the secure dashboard...")
    driver.get("https://httpbin.org/cookies")
    # 6. Validate that the browser successfully authenticated using the injected cookie
    page_text = driver.find_element(By.TAG_NAME, "body").text
    assert "secure_hybrid_token_123" in page_text
    print("[UI] Assertion Passed! We are logged in without ever touching the UI login screen!")
    time.sleep(2) # Paused just so you can see it
    driver.quit()