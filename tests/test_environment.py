def test_homepage_loads_correctly(driver, base_url):
    # Notice we do NOT hardcode the URL! We use the fixture variable!
    print(f"\nNavigating to environment URL: {base_url}")
    driver.get(base_url)
    assert "MyCodeYatra" in driver.title