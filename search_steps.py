from behave import given, when, then
from selenium.webdriver.common.by import By
@given('the user navigates to the store homepage')
def step_impl(context):
    context.driver.get("https://mycodeyatra.com/store")
@when('the user searches for the product "{query}"')
def step_impl(context, query):
    search_box = context.driver.find_element(By.ID, "search-bar")
    search_box.send_keys(query)