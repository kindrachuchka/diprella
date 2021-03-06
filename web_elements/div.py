from selenium.webdriver.remote.webelement import WebElement

from web_elements.abstract_web_element import ABSWebElement


class Div(ABSWebElement):

    def __init__(self, web_element: WebElement):
        super().__init__(web_element)

    def click(self):
        self.web_element.click()