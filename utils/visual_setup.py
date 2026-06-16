from selenium import webdriver
def capture_baseline():
    driver = webdriver.Chrome()
    # We MUST set a strict window size! 
    # If the window size changes, the pixel layout changes, and the test fails!
    driver.set_window_size(1280, 800)
    driver.get("https://httpbin.org/")
    print("\n[Visual] Capturing Golden Baseline Image...")
    driver.save_screenshot("baseline.png")
    driver.quit()
if __name__ == "__main__":
    capture_baseline()