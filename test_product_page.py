import pytest

from .pages.basket_page import BasketPage
from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.product_page import ProductPage



@pytest.mark.add_to_cart
@pytest.mark.parametrize('i', [i for i in range(10) if i != 7])
def test_guest_can_add_product_to_basket(browser, i):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{i}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_to_cart()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    page.should_be_cost_of_the_basket_is_equal_to_the_price_of_the_product()
    page.should_be_message_add_to_basket_has_correct_product_name()
    page.should_be_message_add_to_basket()



@pytest.mark.no_message
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.no_message
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.message_add_to_cart_is_disappeared()

@pytest.mark.login_page_from
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.login_page_from
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.xfail(reason="fixing this bug right now")
def test_guest_can_add_product_to_basket_in_offer7(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_click_add_to_cart()
    base_page = BasePage(browser, link)
    base_page.solve_quiz_and_get_code()
    page.should_be_cost_of_the_basket_is_equal_to_the_price_of_the_product()
    page.should_be_message_add_to_basket_has_correct_product_name()
    page.should_be_message_add_to_basket()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.click_basket_button()
    basket_page = BasketPage(browser, link)
    basket_page.should_not_be_items_in_cart()
    basket_page.should_be_cart_is_empty_text()

