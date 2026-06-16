import requests
import logging
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        # Setup basic logging for the API Client
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("APIClient")
    def authenticate(self, username, password):
        """Authenticates and attaches the token to all future requests."""
        self.logger.info(f"Authenticating as {username}...")
        # Pretend we hit a login endpoint that returns a token
        payload = {"email": username, "password": password}
        response = self.session.post(f"{self.base_url}/login", json=payload)
        if response.status_code == 200:
            token = response.json().get("token")
            self.session.headers.update({"Authorization": f"Bearer {token}"})
            self.logger.info("Authentication Successful! Token attached to Session.")
        else:
            self.logger.error("Authentication Failed!")
            raise Exception("Login Failed")
    def get(self, endpoint, params=None):
        self.logger.info(f"GET Request to {endpoint}")
        return self.session.get(f"{self.base_url}{endpoint}", params=params)
    def post(self, endpoint, payload):
        self.logger.info(f"POST Request to {endpoint} with data: {payload}")
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)