import random
import string
class DataUtils:
    @staticmethod
    def generate_random_email(domain="test.com"):
        """Generates a random 10-character email address."""
        letters = string.ascii_lowercase
        random_str = ''.join(random.choice(letters) for i in range(10))
        email = f"{random_str}@{domain}"
        print(f"Generated Random Email: {email}")
        return email