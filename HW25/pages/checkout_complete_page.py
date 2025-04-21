from ..pages.base_page import BasePage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class CheckoutCompletePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.complete_header = (By.CLASS_NAME, 'complete-header')
        self.back_home_button = (By.ID, 'back-to-products')

    def is_complete_header_text_correct(self):
        return self.is_element_text_correct(self.complete_header, 'Thank you for your order!')

    def back_home(self):
        self.click_button(self.back_home_button)
        return self.is_url_correct(Env.URL_Inventory)
