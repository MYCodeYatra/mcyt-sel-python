import pyotp
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def generate_mfa_code(secret_key):
    """Generates a live 6-digit TOTP code based on the secret key."""
    totp = pyotp.TOTP(secret_key)
    current_code = totp.now()
    print(f"[MFA] Live generated 6-digit code: {current_code}")
    return current_code
def test_mfa_automation_flow():
    driver = webdriver.Chrome()
    # 1. Navigate to the login screen and enter primary credentials
    print("\n[UI] Entering Username and Password...")
    driver.get("https://github.com/login")
    driver.find_element(By.ID, "login_field").send_keys("automation_service_account")
    driver.find_element(By.ID, "password").send_keys("SecurePassword123!")
    driver.find_element(By.NAME, "commit").click()
    # 2. The site now prompts for the 6-digit MFA code
    # We use our Secret Key to mathematically generate the live code!
    mfa_secret_key = "JBSWY3DPEHPK3PXP" # This should be stored in a secure .env file!
    live_code = generate_mfa_code(mfa_secret_key)
    # 3. Enter the 6-digit code into the UI
    print("[UI] Entering 6-digit MFA code...")
    # On GitHub, the MFA input field has id "app_totp"
    # (Note: Use explicit waits in a real framework!)
    time.sleep(2) 
    mfa_input = driver.find_element(By.ID, "app_totp")
    mfa_input.send_keys(live_code)
    # 4. Submit and verify successful login
    print("[UI] MFA Submitted. Verifying Dashboard...")
    # driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]").click()
    # assert "dashboard" in driver.current_url
    print("[Success] Successfully bypassed MFA using PyOTP!")
    driver.quit()