import allure
@allure.epic("E-Commerce Portal")
@allure.feature("Checkout System")
@allure.story("Credit Card Processing")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Verify Visa cards process successfully")
def test_visa_checkout(driver):
    with allure.step("Navigate to the Checkout Page"):
        driver.get("https://mycodeyatra.com/checkout")
    with allure.step("Enter Visa Card Details"):
        # Intentionally failing the assertion to trigger our screenshot hook!
        title = driver.title
        assert "Success" in title, f"Expected 'Success', but got '{title}'"