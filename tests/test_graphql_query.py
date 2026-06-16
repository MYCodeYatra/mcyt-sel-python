import requests
def test_fetch_user_graphql():
    url = "https://api.mycodeyatra.com/graphql"
    # 1. Define the GraphQL Query String
    graphql_query = """
    query GetUser {
        user(id: "101") {
            id
            name
            email
        }
    }
    """
    # 2. Package it into a JSON dictionary
    payload = {
        "query": graphql_query
    }
    # 3. Send the POST request
    response = requests.post(url, json=payload)
    # 4. Assertions!
    assert response.status_code == 200
    # GraphQL always returns data wrapped in a "data" object!
    response_json = response.json()
    assert "errors" not in response_json, "GraphQL returned an error!"
    user_data = response_json["data"]["user"]
    assert user_data["name"] == "Automation Admin"
    assert "email" in user_data