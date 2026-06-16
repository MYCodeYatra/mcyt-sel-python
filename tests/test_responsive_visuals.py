import os
import pytest
from selenium import webdriver
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
# Define our Viewport Matrix
VIEWPORTS = [
    ("Desktop", 1920, 1080),
    ("Tablet", 768, 1024),
    ("Mobile", 390, 844)
]
@pytest.fixture(scope="function")
def driver():
    # Setup Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new") # Run headless for faster execution
    driver_instance = webdriver.Chrome(options=options)
    yield driver_instance
    driver_instance.quit()
@pytest.mark.parametrize("device_name, width, height", VIEWPORTS)
def test_responsive_homepage(driver, device_name, width, height):
    # 1. Resize the browser to simulate the specific device
    driver.set_window_size(width, height)
    # 2. Navigate to the application
    driver.get("https://httpbin.org/")
    # 3. Capture the current state, naming it dynamically!
    current_image = f"current_homepage_{device_name}.png"
    print(f"\n[Visual] Capturing {device_name} viewport ({width}x{height})...")
    driver.save_screenshot(current_image)
    # 4. Perform Visual Comparison (Assuming baselines are already stored locally)
    baseline_image = f"baseline_homepage_{device_name}.png"
    # If the baseline doesn't exist, we save the current image as the new golden baseline!
    if not os.path.exists(baseline_image):
        print(f"⚠️ No baseline found for {device_name}! Establishing new golden baseline.")
        os.rename(current_image, baseline_image)
        assert True
        return
    # 5. Compare the Pixels
    print(f"[Visual] Comparing {device_name} against the Golden Baseline...")
    img_baseline = Image.open(baseline_image)
    img_current = Image.open(current_image)
    img_diff = Image.new("RGBA", img_baseline.size)
    mismatch = pixelmatch(img_baseline, img_current, img_diff, threshold=0.1)
    # Cleanup
    os.remove(current_image)
    assert mismatch < 50, f"UI Regression on {device_name}! {mismatch} pixels changed."
    print(f"✅ {device_name} Viewport is pixel-perfect!")