import time
from selenium import webdriver
def launch_and_hold_browser():
    # 1. Launch a new browser normally
    driver = webdriver.Chrome()
    driver.get("https://mycodeyatra.com")
    # 2. Extract the Executor URL and Session ID
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    print(f"\n[Browser Launched]")
    print(f"Executor URL: {executor_url}")
    print(f"Session ID:   {session_id}")
    print("\nThe browser is now open. Run `hijack_session.py` to control it!")
    # Keep the script alive so the browser doesn't close
    time.sleep(300)
if __name__ == "__main__":
    launch_and_hold_browser()