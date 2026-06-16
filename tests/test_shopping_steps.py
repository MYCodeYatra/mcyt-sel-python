import pytest
from pytest_bdd import scenarios, given, when, then
from selenium.webdriver.common.by import By
scenarios('../features/shopping.feature')
# 1. Create a dictionary fixture to hold our shared context!
@pytest.fixture
def context():
    return {}
@given('the user adds an item to the cart')
def add_item(driver):
    driver.find_element(By.ID, "add-to-cart-btn").click()
@when('the user completes the checkout process')
def complete_checkout(driver, context):
    driver.find_element(By.ID, "checkout-btn").click()
    # Extract the newly generated Order ID from the UI
    order_id = driver.find_element(By.ID, "generated-order-id").text
    # SAVE the Order ID into our shared context dictionary!
    context['order_id'] = order_id
@then('the confirmation page should display the generated order number')
def verify_order_number(driver, context):
    # RETRIEVE the Order ID from the context
    expected_order_id = context['order_id']
    displayed_text = driver.find_element(By.ID, "confirmation-message").text
    assert expected_order_id in displayed_text