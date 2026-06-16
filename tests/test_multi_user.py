import time
from selenium import webdriver
def test_admin_and_customer_simultaneously():
    # 1. Launch the Customer Browser
    customer_driver = webdriver.Chrome()
    # 2. Launch the Admin Browser
    admin_driver = webdriver.Chrome()
    # 3. Position the windows side-by-side so we can watch them!
    customer_driver.set_window_rect(x=0, y=0, width=960, height=1080)
    admin_driver.set_window_rect(x=960, y=0, width=960, height=1080)
    print("\n[Multi-User] Both browsers launched successfully!")
    # 4. Navigate both browsers independently
    customer_driver.get("https://httpbin.org/basic-auth/customer/pass")
    admin_driver.get("https://httpbin.org/basic-auth/admin/pass")
    # Because httpbin uses basic auth, the URL will trigger a 401 prompt.
    # In a real app, you would execute the login flow for both drivers here.
    print(f"[Customer Browser] URL: {customer_driver.current_url}")
    print(f"[Admin Browser] URL: {admin_driver.current_url}")
    # 5. Clean up both drivers!
    time.sleep(2)
    customer_driver.quit()
    admin_driver.quit()