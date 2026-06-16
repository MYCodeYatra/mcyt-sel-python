from selenium import webdriver
def test_extract_jwt_from_local_storage():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.org/")
    # 1. Simulate a React App saving a JWT into Local Storage
    print("\n[Browser] Injecting dummy JWT into Local Storage...")
    driver.execute_script("window.localStorage.setItem('auth_token', 'eyJhbGciOiJIUzI1Ni...SecureData');")
    # 2. Extract the JWT using Python!
    # We use 'return' in our JS string to send the data back to Python
    print("[Python] Attempting to extract token...")
    extracted_token = driver.execute_script("return window.localStorage.getItem('auth_token');")
    print(f"[Success] Extracted Token: {extracted_token}")
    assert extracted_token.startswith("eyJhb")
    # 3. Clear Local Storage to "Log Out"
    driver.execute_script("window.localStorage.removeItem('auth_token');")
    # or clear everything: driver.execute_script("window.localStorage.clear();")
    driver.quit()