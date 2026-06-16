from selenium import webdriver
def reuse_existing_session(executor_url, session_id):
    # 1. Create a "Remote" WebDriver pointing to the existing ChromeDriver server
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=executor_url, options=options)
    # BUG FIX: Selenium creates a new session by default when calling Remote().
    # We must explicitly overwrite the new session ID with our existing one!
    driver.close() # Close the accidentally opened second window
    driver.session_id = session_id # Inject the hijacked Session ID
    print(f"\n[Hijacked!] Successfully connected to Session: {driver.session_id}")
    # 2. Control the existing browser!
    print(f"Current Title: {driver.title}")
    # Navigate the hijacked browser to a new page
    driver.get("https://github.com")
    print(f"Navigated existing browser to: {driver.current_url}")
if __name__ == "__main__":
    # Paste the values from the first script here:
    URL = "http://localhost:12345"
    SESSION = "abcdef1234567890"
    reuse_existing_session(URL, SESSION)