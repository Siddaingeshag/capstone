from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class DemoblazeOperationsPage:
    """
    Page Object for demonstrating Waits and Alerts on demoblaze.com.
    """

    def __init__(self, driver):
        self.driver = driver
        # URL for a specific product page
        self.product_url = "https://www.demoblaze.com/prod.html?idp_=1"
        self.add_to_cart_button = (By.CSS_SELECTOR, ".btn-success")

    def open_product_page(self):
        """Navigates to the Samsung galaxy s6 product page."""
        self.driver.get(self.product_url)

    def add_product_to_cart_and_handle_alert(self):
        """
        Demonstrates an explicit wait and alert handling.
        1. Clicks the 'Add to cart' button.
        2. Waits for the confirmation alert to appear.
        3. Accepts the alert.
        Returns:
            str: The text from the JavaScript alert.
        """
        self.open_product_page()

        # --- Wait Demonstration ---
        # Wait for a maximum of 10 seconds for the 'Add to cart' button to be clickable
        wait = WebDriverWait(self.driver, 10)
        add_cart_btn = wait.until(
            EC.element_to_be_clickable(self.add_to_cart_button)
        )
        add_cart_btn.click()

        # --- Alert Demonstration ---
        # Wait for the alert to be present
        wait.until(EC.alert_is_present())

        # Switch to the alert
        alert = self.driver.switch_to.alert

        # Get the text from the alert
        alert_text = alert.text

        # Accept the alert
        alert.accept()

        return alert_text
