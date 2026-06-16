import logging
import os
from dotenv import load_dotenv
class SensitiveDataFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        load_dotenv()
        # Create a list of all sensitive strings that must never be printed
        self.secrets = [os.getenv("QA_ADMIN_PASS", "DEFAULT_DO_NOT_USE")]
    def filter(self, record):
        # Scan the log message. If a secret is found, replace it with ***
        message = record.getMessage()
        for secret in self.secrets:
            if secret and secret in message:
                message = message.replace(secret, "********")
        record.msg = message
        return True
# Setup secure logger
logger = logging.getLogger("DevSecOps")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.addFilter(SensitiveDataFilter())
logger.addHandler(handler)
def test_log_scrubbing():
    print("\n[Logging] Demonstrating Secure Log Scrubbing...")
    load_dotenv()
    password = os.getenv("QA_ADMIN_PASS", "SuperSecretAdmin123!")
    # Attempting to print the password via our secure logger
    logger.info(f"Attempting to login with password: {password}")