import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def test_azure_ad_sso():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15) # Generous wait for SSO redirects
    # 1. Start at the Application (This will redirect to Microsoft)
    print("\n[SSO] Navigating to target application...")
    # In a real environment, this would be your corporate app.
    # For this simulation, we will go directly to Microsoft's login page.
    driver.get("https://login.microsoftonline.com/")
    # 2. Enter Email
    print("[SSO] Waiting for Email input...")
    email_field = wait.until(EC.element_to_be_clickable((By.NAME, "loginfmt")))
    email_field.send_keys("test_user@mycodeyatra.com")
    # Click Next
    driver.find_element(By.ID, "idSIButton9").click()
    # 3. Enter Password
    # CRITICAL: We MUST wait for the password field to become visible, because 
    # Microsoft executes a massive JavaScript DOM reload here!
    print("[SSO] Email submitted. Waiting for Password input...")
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "passwd")))
    password_field.send_keys("SecurePassword123!")
    # Click Sign In
    driver.find_element(By.ID, "idSIButton9").click()
    # 4. Handle the "Stay Signed In?" prompt
    print("[SSO] Password submitted. Handling 'Stay Signed In' prompt...")
    stay_signed_in_btn = wait.until(EC.element_to_be_clickable((By.ID, "idSIButton9")))
    stay_signed_in_btn.click()
    # 5. Wait for the final redirect back to the application!
    print("[SSO] Authentication complete! Waiting for application redirect...")
    wait.until(EC.url_contains("mycodeyatra")) # Or whatever your app domain is
    print("[SSO] Successfully logged into the application via Azure AD!")
    driver.quit()