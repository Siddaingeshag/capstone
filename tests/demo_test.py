import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.demoblaze_operations_page import DemoblazeOperationsPage


@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the WebDriver.
    """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


def test_add_to_cart_and_handle_alert(driver):
    """
    Tests the explicit wait and alert handling on demoblaze.com.
    - Navigates to a product page.
    - Clicks 'Add to cart' (waits for the button).
    - Waits for and accepts the confirmation alert.
    - Verifies the alert text.
    """
    demoblaze_page = DemoblazeOperationsPage(driver)

    # Perform the action and get the text from the alert
    alert_text = demoblaze_page.add_product_to_cart_and_handle_alert()

    # Verify that the correct alert message was displayed
    assert "Product added" in alert_text, f"Alert text was '{alert_text}', expected 'Product added'."
    print(f"\nSuccessfully handled alert with text: '{alert_text}'")
