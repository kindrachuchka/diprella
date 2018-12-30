from allure_commons._allure import step, attach
from allure import attachment_type
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.abstract_page_object import AbstractPage
from page_objects.login_page import LoginPage
from web_elements.button import Button
from web_elements.find_by import find_by_xpath


class MainPage(AbstractPage):

    def __init__(self, web_driver: WebDriver, url):
        super().__init__(web_driver)
        self.web_driver.maximize_window()
        self.web_driver.get(url)
        attach(
            self.web_driver.get_screenshot_as_png(),
            name="Main Page screenshot",
            attachment_type=attachment_type.PNG
        )

    @property
    @find_by_xpath("//*[@routerlink='/sign-in']", Button)
    def sign_in_button(self):
        pass

    def click_on_sign_up_button(self):
        self.sign_in_button.click()
        return LoginPage(self.web_driver)
