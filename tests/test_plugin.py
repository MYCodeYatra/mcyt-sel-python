# No imports needed! The 'driver' fixture is provided by our Plugin!
def test_plugin_magic(driver):
    driver.get("https://mycodeyatra.com")
    assert "MyCodeYatra" in driver.title