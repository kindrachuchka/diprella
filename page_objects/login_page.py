from allure import attachment_type
from allure_commons._allure import step, attach
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.abstract_sign_page import AbstractSignPage
from page_objects.user_workspace import UserWorkSpacePage
from web_elements.a import A
from web_elements.find_by import find_by_xpath, find_by_class_name


class LoginPage(AbstractSignPage):

    def __init__(self, web_driver: WebDriver):
        super().__init__(web_driver)
        attach(
            self.web_driver.get_screenshot_as_png(),
            name="Login Page screenshot",
            attachment_type=attachment_type.PNG
        )

    @step("Fill in username info")
    def enter_login(self, username):
        with step(f"Username to enter: {username}"):
            self.username_field.click()
            self.username_field.fill_field(username)
        return self

    @step("Fill in password info")
    def enter_password(self, password):
        with step(f"Password to enter: {password}"):
            self.password_field.click()
            self.password_field.fill_field(password)
        return self

    @step("Submitting login button and redirecting to the User Workspace")
    def click_on_login_button(self):
        self.login_button.click()
        return UserWorkSpacePage(self.web_driver)

    @property
    @find_by_xpath('//*[@class="error__text"]', A)
    def forbidden_text(self):
        pass