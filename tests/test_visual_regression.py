import os
from selenium import webdriver
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
def test_homepage_visual_regression():
    # 1. Setup the browser with the exact same dimensions as the baseline
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 800)
    driver.get("https://httpbin.org/")
    # 2. Capture the current state
    current_image_path = "current.png"
    driver.save_screenshot(current_image_path)
    driver.quit()
    # 3. Load both images using Pillow
    print("\n[Visual] Analyzing Pixels...")
    img_baseline = Image.open("baseline.png")
    img_current = Image.open(current_image_path)
    # Create a blank image to store the visual differences
    img_diff = Image.new("RGBA", img_baseline.size)
    # 4. Compare the pixels!
    # includeAA=True ensures that anti-aliasing (smooth font rendering) doesn't cause false positives!
    mismatch_pixels = pixelmatch(
        img_baseline, 
        img_current, 
        img_diff, 
        includeAA=True, 
        threshold=0.1
    )
    print(f"[Visual] Found {mismatch_pixels} mismatched pixels.")
    # 5. If differences are found, save the diff image for the developer
    if mismatch_pixels > 0:
        img_diff.save("visual_diff_report.png")
        print(f"🚨 VISUAL BUG DETECTED! View visual_diff_report.png for details.")
    # 6. Assert the UI is identical (Allowing a tiny 50 pixel variance for rendering differences)
    assert mismatch_pixels < 50, f"UI Regression Detected! {mismatch_pixels} pixels changed!"