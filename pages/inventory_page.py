from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    """
    Page Object for the Sauce Demo Inventory/Products Page.
    """
    def __init__(self, driver):
        self.driver = driver
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")
        self.inventory_container = (By.ID, "inventory_container")

    def is_login_successful(self):
        """
        Verifies if the login was successful by checking for the inventory container.
        Returns:
            bool: True if inventory container is visible, False otherwise.
        """
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.inventory_container)
            )
            return True
        except:
            return False

    def click_menu(self):
        """
        Clicks the burger menu button to open the sidebar.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_button)
        ).click()

    def click_logout(self):
        """
        Clicks the logout link from the sidebar menu.
        """
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.logout_link)
        ).click()

    def logout(self):
        """
        Performs a full logout sequence.
        """
        self.click_menu()
        self.click_logout()
