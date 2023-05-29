from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators
import string
import random


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert "login" in current_url, f" Нет подстроки login в URL{current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Отсутствует форма авторизации на странице"

    def should_be_register_form(self):
        assert self.is_element_present(
            *LoginPageLocators.FORM_REGISTRATION), "Отсутствует форма регистрации на странице"

