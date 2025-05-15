import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from ..pages.login_page import LoginPage
from ..test_data.env import Env


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
    yield browser
    browser.quit()


@pytest.fixture()
def login_p(driver):
    login_page = LoginPage(driver, Env.URL_Login)
    login_page.open()
    return login_page
