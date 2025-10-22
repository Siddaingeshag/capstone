from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductModule:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_first_product_to_cart(self):
        """Add the first product (e.g., 'Sauce Labs Backpack') to cart"""
        add_to_cart_btn = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_btn.click()

    def go_to_cart(self):
        """Click the cart icon to go to cart page"""
        cart_link = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()

    def is_product_in_cart(self, product_name="Sauce Labs Backpack"):
        """Verify product is in cart by checking item name"""
        self.go_to_cart()
        try:
            product = self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
            )
            return product_name in product.text
        except:
            return False

    def remove_first_product_from_cart(self):
        """Remove the first product from cart (if on product page)"""
        remove_btn = self.driver.find_element(By.ID, "remove-sauce-labs-backpack")
        if remove_btn.is_displayed():
            remove_btn.click()