from .base_page import BasePage


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

        # alert = self.browser.switch_to.alert
        # alert.accept()
