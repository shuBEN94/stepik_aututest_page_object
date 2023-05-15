from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.SEE_BASKET_BUTTON)
        basket_button.click()

    def should_be_empty_basket_positive(self):
        empty_basket = self.browser.find_element(*BasePageLocators.EMPTY_BASKET)
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET)
        assert 'Your basket is empty' in empty_basket.text, "Cart is not empty"

    def should_be_empty_basket_negative(self):
        assert self.is_not_element_present(*BasePageLocators.ITEMS_IN_CART), "There is some items in cart"