import time

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.should_be_add_to_cart_button()
        self.should_be_same_product_name()
        self.should_be_same_product_price()

    def should_be_add_to_cart_button(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART), "Add to cart button is not presented"
        add_to_cart_button.click()
        self.solve_quiz_and_get_code()

    def should_be_same_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_in_cart_name = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_NAME)
        assert product_name.text in product_in_cart_name.text, "Product name in cart is incorrect"

    def should_be_same_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_in_cart_price = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_CART_PRICE)
        assert product_price.text in product_in_cart_price.text, "Product price in cart is incorrect"
