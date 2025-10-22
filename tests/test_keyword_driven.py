import json
import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


KEYWORDS_FILE = os.path.join(os.path.dirname(__file__), "..", "keywords", "keywords.json")


def load_keywords():
    with open(KEYWORDS_FILE) as f:
        return json.load(f)


def execute_keyword(driver, action, value=None):
    kw = load_keywords()
    wait = WebDriverWait(driver, 10)  # ✅ Correct: use WebDriverWait from Selenium

    if action == "open_browser":
        driver.get(value or kw["open_browser"])
    elif action == "enter_username":
        wait.until(EC.visibility_of_element_located((By.ID, kw["enter_username"]))).send_keys(value)
    elif action == "enter_password":
        driver.find_element(By.ID, kw["enter_password"]).send_keys(value)
    elif action == "click_login":
        driver.find_element(By.ID, kw["click_login"]).click()
    elif action == "verify_login":
        return wait.until(EC.presence_of_element_located((By.CLASS_NAME, kw["verify_login"]))).is_displayed()
    elif action == "verify_error":
        error_elem = driver.find_element(By.CSS_SELECTOR, kw["verify_error"])
        return "Epic sadface" in error_elem.text
    return None


def test_login_keyword_driven(driver):
    # ✅ No need to attach anything to pytest
    execute_keyword(driver, "open_browser")
    execute_keyword(driver, "enter_username", "standard_user")
    execute_keyword(driver, "enter_password", "secret_sauce")
    execute_keyword(driver, "click_login")
    assert execute_keyword(driver, "verify_login"), "Login failed!"