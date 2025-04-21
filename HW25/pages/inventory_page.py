from ..pages.base_page import BasePage
from ..pages.cart_page import CartPage
from ..test_data.env import Env
from selenium.webdriver.common.by import By


class InventoryPage(BasePage):
    def __init__(self, driver, url):
        super().__init__(driver, url)
        self.add_to_cart = (By.ID, 'add-to-cart-sauce-labs-bike-light')
        self.cart_badge = (By.CLASS_NAME, 'shopping_cart_badge')
        self.remove = (By.ID, 'remove-sauce-labs-bike-light')
        self.cart_link = (By.CLASS_NAME, 'shopping_cart_link')
        self.redirect_page_title = (By.CLASS_NAME, 'title')

    def add_one_item_to_cart(self):
        self.click_button(self.add_to_cart)

    def is_add_item_successful(self):
        url_check = self.is_url_correct(Env.URL_Inventory)
        cart_badge_check = self.is_element_present(self.cart_badge)
        return url_check and cart_badge_check

    def is_number_of_cart_items_n(self, number):
        try:
            cart_badge_text = self.driver.find_element(*self.cart_badge).text
            return cart_badge_text == number
        except:
            return False

    def is_add_product_button_removed(self):
        return not self.is_element_present(self.add_to_cart)

    def is_removed_button_present(self):
        return self.is_element_present(self.remove)

    def navigate_to_cart(self):
        self.add_one_item_to_cart()
        self.click_button(self.cart_link)
        return CartPage(self.driver, self.url)

    def is_navigate_to_cart_successful(self):
        url_check = self.is_url_correct(Env.URL_Cart)
        title_check = self.is_element_text_correct(self.redirect_page_title, 'Your Cart')
        return url_check and title_check
