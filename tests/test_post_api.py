import requests
def test_create_user_statically():
    url = "https://reqres.in/api/users"
    # 1. Define the Payload as a Python Dictionary
    payload = {
        "name": "Morpheus",
        "job": "Leader"
    }
    # 2. Make the POST Request using the `json` argument
    response = requests.post(url, json=payload)
    # 3. Print the response to see the newly created data
    print(f"\nStatus Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
    # 4. A successful POST request usually returns a 201 Created status!
    assert response.status_code == 201