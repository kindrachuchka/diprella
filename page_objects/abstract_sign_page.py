from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.abstract_page_object import AbstractPage
from web_elements.find_by import find_by_class_name, find_by_xpath
from web_elements.a import A
from web_elements.text_field import TextField
from web_elements.button import Button


class AbstractSignPage(AbstractPage):
    def __init__(self, web_driver: WebDriver):
        super().__init__(web_driver)

    @property
    @find_by_class_name("facebook", A)
    def facebook_login_button(self):
        pass

    @property
    @find_by_class_name("google", A)
    def google_login_button(self):
        pass

    @property
    @find_by_class_name("linkedin", A)
    def linkedin_login_button(self):
        pass

    @property
    @find_by_xpath("//*[@formcontrolname='email']", TextField)
    def username_field(self):
        pass

    @property
    @find_by_xpath("//*[@type='password']", TextField)
    def password_field(self):
        pass

    @property
    @find_by_xpath("//*[@type='submit']", Button)
    def login_button(self):
        pass
