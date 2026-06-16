from faker import Faker
class UserBuilder:
    def __init__(self):
        self.faker = Faker()
        # Set default, randomized values for EVERYTHING!
        self.user_data = {
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.email(),
            "phone": self.faker.phone_number()
        }
    # Step-by-step modifier methods
    def with_first_name(self, first_name):
        self.user_data["first_name"] = first_name
        return self  # CRITICAL: Returning self allows method chaining!
    def with_email(self, email):
        self.user_data["email"] = email
        return self
    def without_phone(self):
        self.user_data["phone"] = ""
        return self
    # The final build method returns the constructed dictionary (or object)
    def build(self):
        return self.user_data