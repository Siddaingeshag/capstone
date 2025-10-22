# scroll_test.py
import time
import pytest
from selenium.webdriver.common.by import By


def test_scroll_up_down_inventory_page(driver):
    """
    Test that logs into SauceDemo and performs scroll operations
    on the inventory (product listing) page.
    """
    # Step 1: Go to the login page
    driver.get("https://www.saucedemo.com/")

    # Step 2: Log in with standard user credentials
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    login_button.click()

    # Step 3: Verify successful login (check URL or presence of product list)
    assert "inventory.html" in driver.current_url, "Login failed – not redirected to inventory page."

    # Optional: Wait for products to load (implicit wait already set in conftest)
    time.sleep(1)

    # Step 4: Scroll down to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)  # Visual pause (you'll see it in headed mode)

    # Step 5: Scroll back to the top
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # Step 6: Scroll to a specific product (e.g., the first inventory item)
    first_product = driver.find_element(By.CLASS_NAME, "inventory_item")
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", first_product)
    time.sleep(1)

    # Step 7: Save a screenshot as proof of scroll (optional but helpful)
    driver.save_screenshot("screenshots/scroll_test_success.png")
    print("\n✅ Scroll test completed successfully. Screenshot saved.")