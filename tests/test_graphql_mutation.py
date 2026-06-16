import requests
def test_update_user_graphql():
    url = "https://api.mycodeyatra.com/graphql"
    # 1. Define the Mutation, accepting a $newName variable
    graphql_mutation = """
    mutation UpdateUser($userId: ID!, $newName: String!) {
        updateUser(id: $userId, name: $newName) {
            user {
                id
                name
            }
        }
    }
    """
    # 2. Define the dynamic variables
    variables = {
        "userId": "101",
        "newName": "Enterprise QA Tester"
    }
    # 3. Package BOTH into the JSON payload
    payload = {
        "query": graphql_mutation,
        "variables": variables
    }
    # 4. Send and Assert
    response = requests.post(url, json=payload)
    assert response.status_code == 200
    json_data = response.json()
    updated_name = json_data["data"]["updateUser"]["user"]["name"]
    assert updated_name == "Enterprise QA Tester"