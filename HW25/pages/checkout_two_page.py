from ..pages.base_page import BasePage
from ..pages.checkout_complete_page import CheckoutCompletePage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class CheckoutTwoPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.cart_item = (By.CLASS_NAME, 'cart_item')
        self.item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.finish_button = (By.ID, 'finish')

    def is_item_present(self):
        return self.is_element_present(self.cart_item)

    def is_item_correct(self):
        return self.is_text_correct(self.item_name, 'Sauce Labs Bike Light')

    def finish_purchase(self):
        self.click_button(self.finish_button)
        return CheckoutCompletePage(self.driver, self.url)

    def is_navigate_to_checkout_complete_successful(self):
        return self.is_url_correct(Env.URL_CheckoutComplete)
