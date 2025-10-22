import pytest
from modules.login_module import LoginModule
from modules.product_module import ProductModule


class TestModularDriven:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")

    def test_login_and_add_product_to_cart(self):
        # Initialize modules
        login = LoginModule(self.driver)
        product = ProductModule(self.driver)

        # Step 1: Login
        login.login("standard_user", "secret_sauce")
        assert login.is_login_successful(), "Login failed!"

        # Step 2: Add first product to cart
        product.add_first_product_to_cart()

        # Step 3: Verify product is in cart
        assert product.is_product_in_cart(), "Product was not added to cart!"

        # Optional: Logout is not needed since session ends with driver.quit()