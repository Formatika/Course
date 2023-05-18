import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)


        # alert = self.browser.switch_to.alert
        # alert.accept()
