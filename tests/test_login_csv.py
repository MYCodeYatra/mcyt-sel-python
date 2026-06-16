import csv
import pytest
from selenium import webdriver
# Helper function to read the CSV and return a list of tuples
def read_csv_data():
    data = []
    with open('users.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader) # Skip the header row!
        for row in reader:
            data.append(tuple(row))
    return data
# Pass the helper function to the parametrize decorator!
@pytest.mark.parametrize("username, password, expected_msg", read_csv_data())
def test_login_from_csv(username, password, expected_msg):
    # ... exact same Selenium logic as before!
    print(f"Testing with: {username}")