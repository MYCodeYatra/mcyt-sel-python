import time
from selenium import webdriver
def test_ui_security_headers():
    driver = webdriver.Chrome()
    # 1. Enable CDP Network Tracking
    driver.execute_cdp_cmd('Network.enable', {})
    security_headers = {}
    # 2. Define a listener to capture response headers
    def capture_headers(event):
        if "response" in event:
            url = event["response"]["url"]
            if url == "https://httpbin.org/get":
                print("\n[CDP] Captured network response for target URL!")
                headers = event["response"]["headers"]
                # Convert all keys to lower case for easy checking
                security_headers.update({k.lower(): v for k, v in headers.items()})
    driver.bidi_connection().session.execute(
        driver.bidi_connection().cdp.get_session_id(),
        "Network.responseReceived",
        capture_headers
    )
    # 3. Navigate to the page
    driver.get("https://httpbin.org/get")
    time.sleep(2) # Give CDP a moment to process the async event
    # Note: httpbin does NOT implement strong security headers, 
    # so we will check for standard headers instead to prove the concept.
    print("[Validation] Checking captured headers...")
    assert "content-type" in security_headers
    assert "access-control-allow-origin" in security_headers
    print("✅ Successfully verified headers directly from the browser's Network tab!")
    driver.quit()