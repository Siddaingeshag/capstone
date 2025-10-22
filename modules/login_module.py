from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        login_btn = self.driver.find_element(By.ID, "login-button")
        login_btn.click()

    def login(self, username, password):
        """Complete login flow"""
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_login_successful(self):
        """Check if redirected to Products page"""
        try:
            inventory = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
            )
            return inventory.is_displayed()
        except:
            return False

    def get_error_message(self):
        """Get login error message if any"""
        try:
            error = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='error']"))
            )
            return error.text
        except:
            return ""