def test_failing_logic(driver):
    driver.get("https://mycodeyatra.com")
    assert "Wrong Title" in driver.title