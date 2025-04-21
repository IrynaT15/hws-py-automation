from selenium.common import NoSuchElementException


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def click_button(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    def input_text(self, locator, text):
        field = self.driver.find_element(*locator)
        field.clear()
        field.send_keys(text)

    def is_url_correct(self, url):
        return self.driver.current_url == url

    def is_element_present(self, locator):
        try:
            self.driver.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    def is_element_text_correct(self, locator, text):
        return self.driver.find_element(*locator).text == text
