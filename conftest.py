import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: en, ru, de, ...")


@pytest.fixture(scope="function")
def browser(request):
    lang = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': lang})
    browser = webdriver.Chrome(options=options)

    yield browser
    browser.quit()
