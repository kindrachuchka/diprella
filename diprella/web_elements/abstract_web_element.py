from selenium.webdriver.remote.webelement import WebElement


class ABSWebElement(object):

    def __init__(self, web_element: WebElement):
        self.__element = web_element

    @property
    def web_element(self):
        return self.__element

    @property
    def tag_name(self):
        return self.web_element.tag_name

    @property
    def text(self):
        return self.web_element.text

    def is_displayed(self):
        return self.__element.is_displayed()

    def is_enabled(self):
        return self.__element.is_enabled()

    def is_selected(self):
        return self.__element.is_selected()

    def get_attribute(self, attr):
        return self.__element.get_attribute(attr)