from selenium.webdriver.remote.webelement import WebElement

from web_elements.abstract_web_element import ABSWebElement


class InputButton(ABSWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    @property
    def text(self):
        return self.web_element.get_attribute("value")

    def click(self):
        self.web_element.click()