from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, '//*[@id="login_link"]')


class LoginPageLocators():
    LOGIN_FORM = (By.XPATH, '//*[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//*[@id="register_form"]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="id_registration-email"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="id_registration-password1"]')
    PASSWORD_CONFIRM_FIELD = (By.XPATH, '//*[@id="id_registration-password2"]')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="register_form"]/button')


class ProductPageLocators():
    ADD_TO_CART = (By.XPATH, '//*[@id="add_to_basket_form"]/button')
    PRODUCT_NAME = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_IN_CART_PRICE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    PRODUCT_IN_CART_NAME = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    SEE_BASKET_BUTTON = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.XPATH, '//*[@id="content_inner"]')
    ITEMS_IN_CART = (By.XPATH, '//*[@id="content_inner"]/div[1]/div/h2')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


