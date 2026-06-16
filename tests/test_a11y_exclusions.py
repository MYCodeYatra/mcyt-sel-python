def test_checkout_accessibility_with_exclusions():
    driver = webdriver.Chrome()
    driver.get("https://mycodeyatra.com/checkout")
    axe = Axe(driver)
    axe.inject()
    # Configure the Axe Run Options
    options = {
        # Ignore the third-party chat widget
        "exclude": [["#intercom-chat-widget"]],
        # Turn off the color-contrast rule globally
        "rules": {
            "color-contrast": {"enabled": False}
        }
    }
    results = axe.run(options=options)
    violations = results.get('violations', [])
    assert len(violations) == 0
    driver.quit()