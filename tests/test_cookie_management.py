import time
from selenium import webdriver
def test_get_browser_cookies():
    driver = webdriver.Chrome()
    # Navigate to a secure site
    driver.get("https://github.com")
    # 1. Retrieve all cookies currently set for this domain
    all_cookies = driver.get_cookies()
    print(f"\nTotal Cookies Found: {len(all_cookies)}")
    # 2. Iterate through and print the name and value of each cookie
    for cookie in all_cookies:
        print(f"Cookie Name: {cookie['name']} | Value: {cookie['value'][:10]}...")
    # 3. Retrieve a specific cookie by Name
    specific_cookie = driver.get_cookie("_gh_sess")
    if specific_cookie:
        print(f"\nFound specific GitHub Session Cookie: {specific_cookie['value'][:20]}...")
    driver.quit()