from ..pages.base_page import BasePage
from ..pages.inventory_page import InventoryPage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.username = (By.ID, 'user-name')
        self.password = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.redirect_page_title = (By.CLASS_NAME, 'title')
        self.error = (By.CLASS_NAME, 'error-button')
        self.error_text = (By.TAG_NAME, 'h3')

    def complete_login(self, name, pswrd):
        self.input_text(self.username, name)
        self.input_text(self.password, pswrd)
        self.click_button(self.login_button)
        return InventoryPage(self.driver, self.url)

    def is_login_successful(self):
        url_check = self.is_url_correct(Env.URL_Inventory)
        title_check = self.is_element_text_correct(self.redirect_page_title, 'Products')
        return url_check and title_check

    def is_login_page(self):
        return self.is_url_correct(Env.URL_Login)

    def is_error_present(self):
        return self.is_element_present(self.error)

    def is_error_for_invalid_creds(self):
        error_message = 'Epic sadface: Username and password do not match any user in this service'
        return self.is_element_text_correct(self.error_text, error_message)

    def is_error_for_missing_username(self):
        error_message = 'Epic sadface: Username is required'
        return self.is_element_text_correct(self.error_text, error_message)

    def is_error_for_missing_password(self):
        error_message = 'Epic sadface: Password is required'
        return self.is_element_text_correct(self.error_text, error_message)

    def is_error_for_locked_user(self):
        error_message = 'Epic sadface: Sorry, this user has been locked out.'
        return self.is_element_text_correct(self.error_text, error_message)
