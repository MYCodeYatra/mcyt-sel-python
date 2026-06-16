from utils.api_client import APIClient
from services.user_service import UserService
def test_enterprise_framework_architecture():
    # 1. Initialize the Core Client
    client = APIClient(base_url="https://reqres.in/api")
    # 2. Authenticate the Session globally
    client.authenticate("eve.holt@reqres.in", "cityslicka")
    # 3. Initialize Domain Services
    user_service = UserService(client)
    # 4. Execute Tests cleanly!
    print("\n--- Executing Tests ---")
    # Test GET
    get_response = user_service.get_all_users(page=2)
    assert get_response.status_code == 200
    print(f"Retrieved {len(get_response.json()['data'])} users from page 2.")
    # Test POST
    post_response = user_service.create_user("Neo", "The One")
    assert post_response.status_code == 201
    print(f"Created User ID: {post_response.json()['id']}")