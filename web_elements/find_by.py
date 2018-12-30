from functools import wraps
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from utils.logging import Logging, logger
from web_elements.abstract_web_element import ABSWebElement
from selenium.webdriver.support import expected_conditions as EC


class find_by(object):
    def __init__(self, by: By, expression: str, web_element_class: ABSWebElement):
        self.by = by
        self.expression = expression
        self.web_element_class = web_element_class

    def __call__(self, f):
        @wraps(f)
        def wrapper(_self):
            logger.info("Searching for WebElement with method {} and expression: {}".format(self.by, self.expression))
            return self.web_element_class(
                WebDriverWait(_self.web_driver, 30).until(
                EC.presence_of_element_located((self.by, self.expression))
            )
            )

        return wrapper


class find_by_id(find_by):

    def __init__(self, _id, web_element_class: ABSWebElement):
        super().__init__(By.ID, _id, web_element_class)


class find_by_xpath(find_by):

    def __init__(self, _xpath, web_element_class: ABSWebElement):
        super().__init__(By.XPATH, _xpath, web_element_class)


class find_by_class_name(find_by):

    def __init__(self, _class_name, web_element_class: ABSWebElement):
        super().__init__(By.CLASS_NAME, _class_name, web_element_class)


class find_by_css_selector(find_by):

    def __init__(self, css_selector, web_element_class: ABSWebElement):
        super().__init__(By.CSS_SELECTOR, css_selector, web_element_class)


class find_by_link_text(find_by):

    def __init__(self, link_text, web_element_class: ABSWebElement):
        super().__init__(By.LINK_TEXT, link_text, web_element_class)
