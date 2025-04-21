import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ..pages.login_page import LoginPage
from ..test_data.env import Env
from ..test_data.user_creds import UserCredentials


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--incognito")

    browser = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture()
def login_p(driver):
    login_page = LoginPage(driver, Env.URL_Login)
    login_page.open()
    return login_page


@pytest.fixture
def logged(login_p):
    return login_p.complete_login(UserCredentials.standard_user, UserCredentials.valid_password)


@pytest.fixture
def cart(logged):
    return logged.navigate_to_cart()


@pytest.fixture
def checkout_one(cart):
    return cart.navigate_to_checkout_step_one_page()


@pytest.fixture
def checkout_two(checkout_one):
    return checkout_one.complete_checkout_form('FN', 'LN', '123')


@pytest.fixture
def complete(checkout_two):
    return checkout_two.finish_purchase()
