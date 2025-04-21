from ..pages.base_page import BasePage
from ..pages.checkout_two_page import CheckoutTwoPage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class CheckoutOnePage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.continue_button = (By.ID, 'continue')
        self.error_text = (By.TAG_NAME, 'h3')
        self.first_name = (By.ID, 'first-name')
        self.last_name = (By.ID, 'last-name')
        self.zip = (By.ID, 'postal-code')
        self.redirect_page_title = (By.CLASS_NAME, 'title')

    def complete_checkout_form(self, fname, lname, zip):
        self.input_text(self.first_name, fname)
        self.input_text(self.last_name, lname)
        self.input_text(self.zip, zip)
        self.click_button(self.continue_button)
        return CheckoutTwoPage(self.driver, self.url)

    def is_redirect_to_checkout_two_successful(self):
        url_check = self.is_url_correct(Env.URL_CheckoutTwo)
        title_check = self.is_element_text_correct(self.redirect_page_title, 'Checkout: Overview')
        return url_check and title_check

    def error_for_missing_fn(self):
        error_message = 'Error: First Name is required'
        return self.is_element_text_correct(self.error_text, error_message)

    def error_for_missing_ln(self):
        error_message = 'Error: Last Name is required'
        return self.is_element_text_correct(self.error_text, error_message)

    def error_for_missing_zip(self):
        error_message = 'Error: Postal Code is required'
        return self.is_element_text_correct(self.error_text, error_message)
