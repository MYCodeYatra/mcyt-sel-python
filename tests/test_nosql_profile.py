import time
from selenium.webdriver.common.by import By
def test_user_profile_nosql_persistence(driver, mongo_client):
    # 1. UI ACTION: Fill out the User Profile Form
    driver.get("https://mycodeyatra.com/profile")
    unique_user = f"QA_User_{int(time.time())}"
    # Fill standard fields
    driver.find_element(By.ID, "username").send_keys(unique_user)
    driver.find_element(By.ID, "age").send_keys("28")
    # Fill nested address fields
    driver.find_element(By.ID, "street").send_keys("123 Automation Lane")
    driver.find_element(By.ID, "city").send_keys("Tech City")
    # Submit the form
    driver.find_element(By.ID, "save-profile-btn").click()
    # 2. UI ASSERTION: Verify the success toast
    toast = driver.find_element(By.ID, "toast-message").text
    assert "Profile updated" in toast
    # 3. NOSQL DATABASE ASSERTION: Query the MongoDB Document!
    print(f"\n[MongoDB] Querying 'user_profiles' collection for username: {unique_user}")
    # Access the specific collection
    collection = mongo_client["user_profiles"]
    # Find the document using a JSON query filter
    mongo_document = collection.find_one({"username": unique_user})
    # Assert the document actually exists!
    assert mongo_document is not None, f"Document for {unique_user} was NOT found in MongoDB!"
    # Assert flat fields
    assert mongo_document["age"] == 28, "Age was saved incorrectly!"
    assert mongo_document["status"] == "active", "Default status was not applied by the backend!"
    # Assert nested fields (The power of NoSQL!)
    assert "address" in mongo_document, "Address object was missing from the JSON document!"
    assert mongo_document["address"]["street"] == "123 Automation Lane"
    assert mongo_document["address"]["city"] == "Tech City"