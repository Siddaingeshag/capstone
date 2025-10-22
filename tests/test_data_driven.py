import os
import pytest
from modules.login_module import LoginModule
from utils.csv_reader import read_login_data  # ← Changed import

# Construct path to test data file (now .csv)
DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "login_data.csv")  # ← .csv


@pytest.mark.parametrize("test_data", read_login_data(DATA_FILE))
def test_login_data_driven(driver, test_data):
    """
    Data-Driven Test: Runs login test for each row in login_data.csv
    """
    # Navigate to SauceDemo (fix extra spaces in URL!)
    driver.get("https://www.saucedemo.com/  ")  # ← Removed extra spaces

    # Initialize login module
    login = LoginModule(driver)

    # Perform login
    login.login(test_data["username"], test_data["password"])

    # Validate result based on 'expected' column
    if test_data["expected"] == "success":
        assert login.is_login_successful(), \
            f"Login failed for valid user: {test_data['username']}"
    else:
        error_msg = login.get_error_message()
        assert "Epic sadface" in error_msg, \
            f"Expected error not shown for invalid user: {test_data['username']}"
