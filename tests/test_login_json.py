import json
import pytest
def read_json_data():
    with open('data.json', 'r') as file:
        raw_data = json.load(file)
        # Convert list of dicts to list of tuples for PyTest
        return [(item['user'], item['pass'], item['msg']) for item in raw_data]
@pytest.mark.parametrize("user, pwd, msg", read_json_data())
def test_login_from_json(user, pwd, msg):
    print(f"Logging in {user} with {pwd} expecting {msg}")
    # ... Selenium logic