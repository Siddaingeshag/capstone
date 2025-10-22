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
    # options.add_argument("--headless")  # Keep disabled to see browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    options.add_argument("--disable-gpu")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


# Hook to capture screenshot on failure AND attach to HTML report
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Only act on actual test failures (not setup/teardown)
    if rep.when == "call" and rep.failed:
        if "driver" in item.funcargs:
            driver = item.funcargs["driver"]
            screenshot_dir = os.path.join(os.path.dirname(__file__), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name.replace("::", "_")
            filename = f"{test_name}_{timestamp}.png"
            filepath = os.path.join(screenshot_dir, filename)

            driver.save_screenshot(filepath)
            print(f"\n📸 Screenshot saved: {filepath}")

            # Attach to HTML report (if pytest-html is available)
            try:
                from pytest_html import extras
                if not hasattr(rep, "extra"):
                    rep.extra = []
                rep.extra.append(extras.png(filepath))
            except ImportError:
                pass  # pytest-html not installed