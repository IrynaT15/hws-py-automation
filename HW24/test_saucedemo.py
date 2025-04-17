import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def login(browser):
    browser.get('https://www.saucedemo.com/')
    username_field = browser.find_element(By.ID, 'user-name')
    username_field.clear()
    username_field.send_keys("standard_user")

    password_field = browser.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys("secret_sauce")

    browser.find_element(By.ID, 'login-button').click()


@pytest.fixture
def add_to_cart(browser, login):
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    return True


def test_login_success(browser, login):
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"
    page_title = browser.find_element(By.CLASS_NAME, 'title')
    assert page_title.text == 'Products'


@pytest.mark.parametrize("username,password", [
    ('test', 'secret_sauce'),
    ('standard_user', 'test'),
    ('', 'secret_sauce'),
    ('standard_user', '')
])
def test_invalid_login(browser, username, password):
    browser.get('https://www.saucedemo.com/')
    username_field = browser.find_element(By.ID, 'user-name')
    username_field.clear()
    username_field.send_keys(username)

    password_field = browser.find_element(By.ID, 'password')
    password_field.clear()
    password_field.send_keys(password)

    browser.find_element(By.ID, 'login-button').click()

    error = browser.find_element(By.CLASS_NAME, 'error-button')
    assert error
    assert browser.current_url == "https://www.saucedemo.com/"


def test_add_an_item_to_empty_cart_success(browser, login):
    add_to_cart_button = browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light')
    add_to_cart_button.click()
    assert browser.current_url == "https://www.saucedemo.com/inventory.html"

    items_in_the_cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    number_of_items_text = items_in_the_cart.text
    assert number_of_items_text == "1"


def test_add_second_item_to_the_cart_success(browser, login):
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
    browser.find_element(By.ID, 'add-to-cart-sauce-labs-backpack').click()
    items_in_the_cart = browser.find_element(By.CLASS_NAME, 'shopping_cart_badge')
    number_of_items_text = items_in_the_cart.text
    assert number_of_items_text == "2"


def test_complete_purchase_success(browser, login, add_to_cart):
    browser.find_element(By.CLASS_NAME, 'shopping_cart_link').click()
    # WebDriverWait(browser, 5).until(EC.url_contains("cart.html"))
    assert browser.current_url == "https://www.saucedemo.com/cart.html"

    page_title = browser.find_element(By.CLASS_NAME, 'title')
    assert page_title.text == 'Your Cart'

    item = browser.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert item.text == 'Sauce Labs Bike Light'

    browser.find_element(By.ID, 'checkout').click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-step-one.html"

    page_title = browser.find_element(By.CLASS_NAME, 'title')
    assert page_title.text == 'Checkout: Your Information'

    fn_field = browser.find_element(By.ID, 'first-name')
    fn_field.clear()
    fn_field.send_keys('Iryna')

    ln_field = browser.find_element(By.ID, 'last-name')
    ln_field.clear()
    ln_field.send_keys('Tain')

    zip_field = browser.find_element(By.ID, 'postal-code')
    zip_field.clear()
    zip_field.send_keys('123-456')

    browser.find_element(By.ID, 'continue').click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-step-two.html"

    page_title = browser.find_element(By.CLASS_NAME, 'title')
    assert page_title.text == 'Checkout: Overview'

    item = browser.find_element(By.CLASS_NAME, 'inventory_item_name')
    assert item.text == 'Sauce Labs Bike Light'

    browser.find_element(By.ID, 'finish').click()
    assert browser.current_url == "https://www.saucedemo.com/checkout-complete.html"

    page_title = browser.find_element(By.CLASS_NAME, 'title')
    assert page_title.text == 'Checkout: Complete!'

    success_message = browser.find_element(By.CLASS_NAME, 'complete-header')
    assert success_message.text == 'Thank you for your order!'
