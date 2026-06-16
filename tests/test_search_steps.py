from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.by import By
# Load the Scenario Outline!
scenarios('../features/search.feature')
@given('the user navigates to the store homepage')
def navigate_home(driver):
    driver.get("https://mycodeyatra.com/store")
@when(parsers.parse('the user searches for the product "{query}"'))
def enter_search(driver, query):
    search_box = driver.find_element(By.ID, "search-bar")
    search_box.clear()
    search_box.send_keys(query)
    driver.find_element(By.ID, "search-submit").click()
@then(parsers.parse('the search results page should display "{expected_text}"'))
def verify_results_text(driver, expected_text):
    header = driver.find_element(By.ID, "search-header").text
    assert expected_text in header
@then(parsers.parse('the total results count should be greater than {min_results}'))
def verify_results_count(driver, min_results):
    # Notice we must cast min_results to an integer!
    count_text = driver.find_element(By.ID, "total-count").text
    assert int(count_text) > int(min_results)