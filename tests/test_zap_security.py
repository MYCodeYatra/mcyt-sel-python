import time
from selenium import webdriver
from zapv2 import ZAPv2
# Configuration
ZAP_PROXY_HOST = "127.0.0.1"
ZAP_PROXY_PORT = 8080
TARGET_URL = "http://public-firing-range.appspot.com/" # A Google test site
def test_passive_security_scan():
    # 1. Configure Selenium to use the ZAP Proxy
    options = webdriver.ChromeOptions()
    options.add_argument(f'--proxy-server=http://{ZAP_PROXY_HOST}:{ZAP_PROXY_PORT}')
    # Ignore certificate errors since ZAP uses a self-signed cert to intercept HTTPS
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    # 2. Connect to the ZAP API
    zap = ZAPv2(proxies={'http': f'http://{ZAP_PROXY_HOST}:{ZAP_PROXY_PORT}', 
                         'https': f'http://{ZAP_PROXY_HOST}:{ZAP_PROXY_PORT}'})
    # 3. Selenium navigates the app normally
    print("\n[Selenium] Navigating the application...")
    driver.get(TARGET_URL)
    # Imagine Selenium clicking through multiple pages here...
    time.sleep(3) # Give ZAP a moment to process the traffic
    driver.quit()
    # 4. Analyze the ZAP Results!
    print("[ZAP] Analyzing captured traffic for vulnerabilities...")
    # Fetch alerts specific to our target URL
    alerts = zap.core.alerts(baseurl=TARGET_URL)
    print(f"\nFound {len(alerts)} potential security vulnerabilities:")
    high_risk_count = 0
    for alert in alerts:
        risk = alert.get('risk')
        name = alert.get('name')
        if risk == "High":
            print(f"🚨 CRITICAL: {name}")
            high_risk_count += 1
        elif risk == "Medium":
            print(f"⚠️ WARNING: {name}")
    # 5. Fail the test if High Risk vulnerabilities exist!
    assert high_risk_count == 0, f"Found {high_risk_count} High Risk Vulnerabilities! Build Failed!"