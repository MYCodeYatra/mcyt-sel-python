import requests
def test_get_user_api():
    # 1. Define the Endpoint URL
    url = "https://reqres.in/api/users/2"
    # 2. Make the GET Request
    response = requests.get(url)
    # 3. Print out the raw data for debugging
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    # 4. Assert the Status Code is 200 (OK)
    assert response.status_code == 200