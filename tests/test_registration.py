from pages.login_page import LoginPage
from utils.data_utils import DataUtils
def test_dynamic_registration(driver):
    login_page = LoginPage(driver)
    # Use the data utility!
    random_email = DataUtils.generate_random_email()
    # The UI utility automatically handles the waits and clicks!
    login_page.login(random_email, "SecurePassword123!")