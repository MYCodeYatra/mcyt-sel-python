class UserService:
    def __init__(self, api_client):
        self.api = api_client
        self.endpoint = "/users"
    def get_all_users(self, page=1):
        return self.api.get(self.endpoint, params={"page": page})
    def create_user(self, name, job):
        payload = {"name": name, "job": job}
        return self.api.post(self.endpoint, payload)