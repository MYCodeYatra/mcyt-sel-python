import time
from selenium import webdriver
 
def test_launch_browser():
    # 1. Initialize the WebDriver (Selenium Manager handles the driver binary automatically!)
    print("\nLaunching Chrome Browser...")
    driver = webdriver.Chrome()
 
    # 2. Maximize the window
    driver.maximize_window()
 
    # 3. Navigate to our practice site
    driver.get("https://mycodeyatra.com")
 
    # 4. Grab the page title
    title = driver.title
    print(f"Page Title is: {title}")
 
    # 5. Sleep for 3 seconds just to visually see it (Never use sleep in real tests!)
    time.sleep(3)
 
    # 6. Quit the browser and kill the process
    driver.quit()