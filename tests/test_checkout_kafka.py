import time
import pytest
from selenium.webdriver.common.by import By
from utils.kafka_helper import get_latest_kafka_message
def test_checkout_fires_kafka_event(driver):
    # 1. UI ACTION: Process an Order
    driver.get("https://mycodeyatra.com/checkout")
    dynamic_order_id = f"ORD_{int(time.time())}"
    # Let's assume the UI has a hidden field or mock input for Order ID for testing purposes
    driver.find_element(By.ID, "item-name").send_keys("Selenium Masterclass Course")
    driver.find_element(By.ID, "customer-email").send_keys("qa@mycodeyatra.com")
    # Click the Checkout Button (This triggers the backend to fire the Kafka event!)
    driver.find_element(By.ID, "complete-order-btn").click()
    # 2. UI ASSERTION: Verify the success screen
    success_text = driver.find_element(By.ID, "order-success-msg").text
    assert "Thank you for your purchase" in success_text
    # 3. KAFKA ASSERTION: Validate the asynchronous event!
    kafka_payload = get_latest_kafka_message(topic="orders.processed")
    # Verify the event actually arrived!
    assert kafka_payload is not None, "Kafka Event was never fired by the backend!"
    # Verify the contents of the Event Payload match the UI actions!
    assert kafka_payload["event_type"] == "OrderPlaced"
    assert kafka_payload["data"]["item"] == "Selenium Masterclass Course"
    assert kafka_payload["data"]["customer"] == "qa@mycodeyatra.com"
    assert kafka_payload["data"]["status"] == "PENDING_SHIPMENT"