import requests
def test_get_users_with_query_params():
    url = "https://reqres.in/api/users"
    # 1. Define your Query Parameters as a Dictionary
    payload = {
        "page": 2,
        "per_page": 3
    }
    # 2. Pass them to the `params` argument
    response = requests.get(url, params=payload)
    # Notice that requests automatically formats the URL for us!
    print(f"\nFinal URL executed: {response.url}")
    json_data = response.json()
    assert response.status_code == 200
    # 3. Validate the API correctly applied the pagination filters
    assert json_data["page"] == 2
    assert json_data["per_page"] == 3