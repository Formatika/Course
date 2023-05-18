from selenium.webdriver.common.by import By


class MainPageLocators():
    pass

class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_CART = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>:nth-child(2)")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>:nth-child(1)")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1)>.alertinner")
    MESSAGE_ADD_TO_BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) strong")
    MESSAGE_BASKET_COST = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3)>.alertinner>p:nth-child(1)")
    MESSAGE_BASKET_COST_PRICE = (By.CSS_SELECTOR, "#messages>.alert:nth-child(3) strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group>a")

class BasketPageLocators:
    CART_ITEMS = (By.CLASS_NAME, "basket-items")
    CART_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")






