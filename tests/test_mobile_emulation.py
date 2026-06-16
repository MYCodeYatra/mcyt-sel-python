from selenium import webdriver
from selenium.webdriver.chrome.options import Options
def test_iphone_emulation():
    # 1. Define the Mobile Emulation Dictionary
    # You can use standard names like 'iPhone 12 Pro', 'Pixel 5', or 'iPad Mini'
    mobile_emulation = {
        "deviceName": "iPhone 12 Pro"
    }
    # 2. Inject it into ChromeOptions
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    # 3. Launch the Emulated Browser
    print("\n[Emulation] Launching Chrome as an iPhone 12 Pro...")
    driver = webdriver.Chrome(options=chrome_options)
    # 4. Navigate to a site that checks User-Agents
    driver.get("https://httpbin.org/user-agent")
    # 5. Extract the User-Agent the server *actually* received
    detected_user_agent = driver.find_element("tag name", "pre").text
    print(f"[Server Response] {detected_user_agent}")
    # Assert that the server truly believes we are on an iPhone!
    assert "iPhone" in detected_user_agent
    assert "Mobile" in detected_user_agent
    print("✅ Successfully tricked the server into serving the Mobile Web architecture!")
    driver.quit()