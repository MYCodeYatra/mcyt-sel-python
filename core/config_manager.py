import os
from dotenv import load_dotenv

load_dotenv()

class ConfigManager:
    BASE_URL = os.getenv("BASE_URL", "https://mycodeyatra.com")
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
    ADMIN_USER = os.getenv("ADMIN_USER", "admin")
    ADMIN_PASS = os.getenv("ADMIN_PASS", "SuperSecret123!")
