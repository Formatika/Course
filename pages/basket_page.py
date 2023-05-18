from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_cart_is_empty_text(self):
        assert self.is_element_present(*BasketPageLocators.CART_IS_EMPTY)

    def should_not_be_items_in_cart(self):
        assert self.is_not_element_present(*BasketPageLocators.CART_ITEMS),\
            "В корзине присутствует товар, но его в действительности быть не должно"