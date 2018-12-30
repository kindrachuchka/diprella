from selenium.webdriver.remote.webelement import WebElement

from web_elements.abstract_web_element import ABSWebElement


class Link(ABSWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    @property
    def href(self):
        return self.web_element.get_property("href")

    def click(self):
        self.web_element.click()