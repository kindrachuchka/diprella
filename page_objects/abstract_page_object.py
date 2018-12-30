from selenium.webdriver.remote.webdriver import WebDriver

from web_elements.find_by import find_by_class_name
from web_elements.span import Span
from web_elements.text_field import TextField


class AbstractPage(object):
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver

    @property
    @find_by_class_name("logo__icon", Span)
    def diprella_logo(self):
        pass

    @property
    @find_by_class_name("header__nav-search", TextField)
    def search_field(self):
        pass