from allure_commons._allure import attach
from allure import attachment_type
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.abstract_page_object import AbstractPage
from web_elements.button import Button
from web_elements.svg import Svg
from web_elements.a import A
from web_elements.find_by import find_by_xpath, find_by_id


class UserWorkSpacePage(AbstractPage):
    def __init__(self, web_driver: WebDriver):
        super().__init__(web_driver)
        attach(
            self.web_driver.get_screenshot_as_png(),
            name="User Workspace Page screenshot",
            attachment_type=attachment_type.PNG
        )

    @property
    @find_by_xpath("//*[@class='home__header-nav-link non--avatar ng-star-inserted']", Button)
    def user_menu(self):
        pass

    @property
    @find_by_xpath('//*[@id="Capa_1"]', Svg)
    def lector_menu(self):
        pass

    @property
    @find_by_xpath('//*[@id="Capa_1"]', Svg)
    def library_menu(self):
        pass

    @property
    @find_by_xpath('//*[@class="error__text"]', A)
    def forbidden_text(self):
        pass

    @property
    @find_by_xpath('//*[@class="recomendations"]', A)
    def recomendations(self):
        pass
