from ..pages.base_page import BasePage
from ..pages.checkout_one_page import CheckoutOnePage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.cart_item = (By.CLASS_NAME, 'cart_item')
        self.item_name = (By.CLASS_NAME, 'inventory_item_name')
        self.checkout = (By.ID, 'checkout')
        self.redirect_page_title = (By.CLASS_NAME, 'title')

    def is_item_correctly_added(self):
        item_presence_check = self.is_element_present(self.cart_item)
        item_name_check = self.is_element_text_correct(self.item_name, 'Sauce Labs Bike Light')
        return item_presence_check and item_name_check

    def navigate_to_checkout_step_one_page(self):
        self.click_button(self.checkout)
        return CheckoutOnePage(self.driver, self.url)

    def is_navigate_to_checkout_step_one_successful(self):
        url_check = self.is_url_correct(Env.URL_CheckoutOne)
        title_check = self.is_element_text_correct(self.redirect_page_title,
                                                   'Checkout: Your Information')
        return url_check and title_check
