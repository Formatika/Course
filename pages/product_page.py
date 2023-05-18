import math

from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException  # в начале файла

from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_click_add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

    def should_be_cost_of_the_basket_is_equal_to_the_price_of_the_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_COST_PRICE).text
        assert product_price == product_price_in_msg, \
            f"Cтоимость продукта в сообщении '{product_price_in_msg}' не совпадает с действительной ценой продукта '{product_price}'"

    def should_be_message_add_to_basket_has_correct_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_msg = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET_PRODUCT_NAME).text
        assert product_name == product_name_in_msg, \
            f"Название продукта в сообщении '{product_name_in_msg}' не соответствует реальному названию продукта '{product_name}'"

    def should_be_message_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Cообщение о добавлении товара в корзину отсутствует"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def message_add_to_cart_is_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Cообщение о добавлении товара в корзину не исчезло"



