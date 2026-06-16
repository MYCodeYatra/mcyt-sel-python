import requests
def test_delete_user():
    # Target an existing user ID (User 2)
    url = "https://reqres.in/api/users/2"
    print(f"\n[DELETE] Attempting to erase resource at {url}")
    # 1. Make the DELETE request
    response = requests.delete(url)
    # 2. Validate the Status Code
    print(f"[DELETE] Server responded with Status Code: {response.status_code}")
    # 204 No Content is the standard success code for a DELETE operation!
    assert response.status_code == 204
    # 3. Assert the response body is empty (No Content!)
    assert response.text == ""