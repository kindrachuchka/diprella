from functools import wraps

import pytest
from allure_commons._allure import attach
from allure import attachment_type
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fOptions

from page_objects.main_page import MainPage
from utils.logging import logger


def pytest_addoption(parser):
    parser.addoption("--firefox",
                     action='store_true',
                     default=False,
                     help="Start Firefox WebDriver")
    parser.addoption("--ie",
                     action='store_true',
                     default=False,
                     help="Start Internet Explorer WebDriver")
    parser.addoption("--google-chrome",
                     action='store_true',
                     default=False,
                     help="Start Google Chrome WebDriver")
    parser.addoption("--webdriver-location",
                     action='store',
                     help="Where to get the webdriver")
    parser.addoption("--path_to_config",
                     action='store',
                     help="Something wrong with path to config")
    # parser.addoption("--positive",
    #                  action="store_true",
    #                  default=False,
    #                  help="Positive or negative data has to be used")
    # parser.addoption("--negative",
    #                  action="store_true",
    #                  default=False,
    #                  help="Positive or negative data has to be used")

def get_env():
    env = list()
    with open(f"{pytest.config.getoption('--path_to_config')}", 'r') as data:
        env = data.readline().split(', ')

    logger.debug(f"Environment: {env}")
    return env

@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    request.cls.webdriver_path = pytest.config.getoption("--webdriver-location")

    if pytest.config.getoption("--firefox"):
        request.cls.webdriver = webdriver.Firefox
    elif pytest.config.getoption("--ie"):
        request.cls.webdriver = webdriver.Ie
    elif pytest.config.getoption("--google-chrome"):
        request.cls.webdriver = webdriver.Chrome
    else:
        raise ValueError("Incorrect browser")


@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    if isinstance(request.cls.webdriver, webdriver.Chrome):
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path, chrome_options=chrome_options)
    elif isinstance(request.cls.webdriver, webdriver.Firefox):
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        _browser_profile.set_preference("dom.push"
                                        ".enabled", False)
        options = fOptions()
        #options.set_headless(headless=True)
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path,
                                                                  firefox_options=options, firefox_profile=_browser_profile)
    else:
        request.cls.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path)
    request.cls.main_page = MainPage(request.cls.initialized_webdriver, get_env()[0])
    def driver_close():
        request.cls.initialized_webdriver.quit()

    request.addfinalizer(driver_close)


# url, username, password
# username2, password
def pytest_generate_tests(metafunc):
        params = tuple(get_env()[1:])
        logger.debug(f"Parameters: {params}")
        metafunc.parametrize("username, password", (
            params,
        ))