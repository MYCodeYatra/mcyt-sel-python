import pytest
from selenium import webdriver
from axe_selenium_python import Axe
def test_homepage_accessibility():
    # 1. Initialize the browser
    driver = webdriver.Chrome()
    driver.get("https://mycodeyatra.com")
    # 2. Initialize the Axe Engine and Inject it into the page
    axe = Axe(driver)
    axe.inject()
    # 3. Run the Accessibility Audit!
    print("\n[a11y] Scanning DOM for WCAG Violations...")
    results = axe.run()
    # 4. Extract the Violations Array
    violations = results.get('violations', [])
    # 5. Assert that the page is 100% compliant
    if len(violations) > 0:
        print(f"\n[Error] Found {len(violations)} accessibility violations!")
        # Print a readable report of what broke
        print(axe.report(violations))
    assert len(violations) == 0, f"Accessibility tests failed! {len(violations)} violations found."
    driver.quit()