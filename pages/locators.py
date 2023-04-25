from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')


class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_IN_CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_IN_CART_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')


