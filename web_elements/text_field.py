from selenium.webdriver.remote.webelement import WebElement

from web_elements.abstract_web_element import ABSWebElement


class TextField(ABSWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    @property
    def text(self):
        return self.web_element.get_attribute("value")

    def fill_field(self, text: str):
        self.web_element.send_keys(text)

    def click(self):
        self.web_element.click()