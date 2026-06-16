import requests
import responses
# We use the @responses.activate decorator to enable the interceptor
@responses.activate
def test_mock_github_api_success():
    url = "https://api.github.com/users/mycodeyatra"
    # 1. Define the Mock (The Interceptor)
    responses.add(
        responses.GET,
        url,
        json={"login": "FakeYatra", "followers": 999999},
        status=200
    )
    # 2. Execute the Request (This will NOT hit the real internet!)
    response = requests.get(url)
    print(f"\n[Mocked] Status Code: {response.status_code}")
    print(f"[Mocked] Response JSON: {response.json()}")
    # 3. Assert our mocked data was returned
    assert response.status_code == 200
    assert response.json()["followers"] == 999999