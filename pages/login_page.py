from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    """
    Page Object for the Sauce Demo Login Page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.url = "https://www.saucedemo.com/"

    def open(self):
        """
        Navigates to the login page.
        """
        self.driver.get(self.url)

    def enter_username(self, username):
        """
        Enters the username into the username field.
        Args:
            username (str): The username to enter.
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_input)
        ).send_keys(username)

    def enter_password(self, password):
        """
        Enters the password into the password field.
        Args:
            password (str): The password to enter.
        """
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """
        Clicks the login button.
        """
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        """
        Performs a full login sequence.
        Args:
            username (str): The username for login.
            password (str): The password for login.
        """
        self.open()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
