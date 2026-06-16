import os
from selenium import webdriver
from PIL import Image
from pixelmatch.contrib.PIL import pixelmatch
from utils.visual_asset_manager import VisualAssetManager
def test_cloud_visual_regression():
    image_name = "homepage_desktop.png"
    asset_manager = VisualAssetManager()
    # 1. Capture Current State
    driver = webdriver.Chrome()
    driver.set_window_size(1280, 800)
    driver.get("https://httpbin.org/")
    current_path = "current_homepage.png"
    driver.save_screenshot(current_path)
    driver.quit()
    # 2. Fetch the Baseline from AWS S3!
    try:
        baseline_path = asset_manager.fetch_baseline(image_name)
    except FileNotFoundError:
        print("\n⚠️ New Visual Test Detected! Uploading current state as the new Golden Baseline...")
        asset_manager.update_baseline(current_path, image_name)
        assert True, "First run completed. Baseline established."
        return
    # 3. Perform the Pixel Comparison
    print("[Visual] Comparing downloaded baseline against current state...")
    img_baseline = Image.open(baseline_path)
    img_current = Image.open(current_path)
    img_diff = Image.new("RGBA", img_baseline.size)
    mismatch = pixelmatch(img_baseline, img_current, img_diff, threshold=0.1)
    # 4. Clean up the downloaded temporary files so we don't bloat the hard drive!
    os.remove(baseline_path)
    os.remove(current_path)
    assert mismatch < 50, f"UI Regression! {mismatch} pixels changed."
    print("✅ Visual Regression Passed! UI perfectly matches Cloud Baseline.")