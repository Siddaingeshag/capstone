import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def driver():
    """
    Pytest fixture to initialize and quit the WebDriver.
    """
    # Initialize the WebDriver
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10) # Implicit wait for elements
    yield driver
    # Teardown: close the browser
    driver.quit()

def test_login_and_logout(driver):
    """
    Test case for logging in and then logging out of Sauce Demo.
    """
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    # --- Login Step ---
    # Perform login using valid credentials
    login_page.login("standard_user", "secret_sauce")

    # --- Verification for Login ---
    # Check if login was successful and we are on the inventory page
    assert inventory_page.is_login_successful(), "Login failed. Inventory page not displayed."
    print("Login Successful!")

    # --- Logout Step ---
    inventory_page.logout()

    # --- Verification for Logout ---
    # Check if we are redirected back to the login page
    assert "saucedemo.com" in driver.current_url and driver.find_element(*login_page.login_button), \
        "Logout failed. Not redirected to the login page."
    print("Logout Successful!")
