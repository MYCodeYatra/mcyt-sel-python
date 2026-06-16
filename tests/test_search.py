from selenium.webdriver.common.by import By
def test_homepage_search(driver):
    driver.get("https://mycodeyatra.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.submit()
    assert "Selenium Python" in driver.title