import requests
from faker import Faker
def test_put_full_update():
    # Target an existing user ID (User 2)
    url = "https://reqres.in/api/users/2"
    fake = Faker()
    new_name = fake.name()
    new_job = "Senior Engineer"
    # 1. Provide the FULL payload
    payload = {
        "name": new_name,
        "job": new_job
    }
    print(f"\n[PUT] Sending full update payload: {payload}")
    # 2. Make the PUT request
    response = requests.put(url, json=payload)
    # 3. Assert a successful 200 OK status
    assert response.status_code == 200
    # 4. Verify the server returned our updated data and a timestamp
    json_data = response.json()
    print(f"[PUT] Server Response: {json_data}")
    assert json_data["name"] == new_name
    assert json_data["job"] == new_job
    assert "updatedAt" in json_data