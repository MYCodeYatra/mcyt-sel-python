import requests
def test_manual_jwt_authentication():
    # 1. Authenticate to get the token
    login_url = "https://reqres.in/api/login"
    credentials = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    login_response = requests.post(login_url, json=credentials)
    assert login_response.status_code == 200
    # Extract the token from the JSON payload
    token = login_response.json()["token"]
    print(f"\n[Login] Extracted Token: {token}")
    # 2. Access a Secure Endpoint
    secure_url = "https://reqres.in/api/users/2" # Pretend this is secure
    # We must manually construct the Authorization header
    auth_headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    # Pass the headers dictionary into the GET request
    secure_response = requests.get(secure_url, headers=auth_headers)
    assert secure_response.status_code == 200
    print("[Secure API] Successfully accessed locked data!")