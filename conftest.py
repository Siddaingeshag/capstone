# conftest.py
import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    # Remove or comment out the headless argument to see the browser
    # options.add_argument("--headless")  # ← DISABLED for headed mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--disable-gpu")

    # Use webdriver-manager to auto-handle ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # Set implicit wait for element stability
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# Optional: Auto-screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("::", "_")
            filepath = os.path.join(screenshot_dir, f"{test_name}_{timestamp}.png")

            driver.save_screenshot(filepath)
            print(f"\n📸 Screenshot saved on failure: {filepath}")