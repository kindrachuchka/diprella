import allure
import pytest
import time


class TestPages(object):

    @allure.title("Login page")
    @allure.description_html("Verifying <b>Login Page</b> contains required elements")
    def test_loginpage(self, username, password):
        with allure.step("Check that Diprella Logo is present on the page and displayed"):
            assert self.main_page.sign_in_button.is_displayed(), "Diprella Logo is not shown"

        login_page = self.main_page.click_on_sign_up_button()
        with allure.step("Check that facebook/google/linkedin Logo is present on the page and displayed"):
            assert login_page.facebook_login_button.is_displayed()
            assert login_page.google_login_button.is_displayed()
            assert login_page.linkedin_login_button.is_displayed()

        with allure.step("Check that login, password fields and login button are present on the page and displayed"):
            assert login_page.username_field.is_displayed()
            assert login_page.password_field.is_displayed()
            assert login_page.login_button.is_displayed()

        login_page.enter_login(username)
        login_page.enter_password(password)

        workspace_page = login_page.click_on_login_button()

        with allure.step("Check if diprella logo is present on the page and displayed"):
            assert workspace_page.diprella_logo.is_displayed(), "UserMenu is not shown"

        with allure.step("Check if Search field is present on the page and displayed"):
            assert workspace_page.search_field.is_displayed(), "UserMenu is not shown"

        with allure.step("Check if User Menu is present on the page and displayed"):
            assert workspace_page.user_menu.is_displayed(), "UserMenu is not shown"

        with allure.step("Check if Lector Menu is present on the page and displayed"):
            assert workspace_page.lector_menu.is_displayed(), "LectorMenu is not shown"

        with allure.step("Check if Library Menu is present on the page and displayed"):
            assert workspace_page.library_menu.is_displayed(), "LibraryMenu is not shown"

        with allure.step("Check if Recomendation section is present on the page and displayed"):
            assert workspace_page.recomendations.is_displayed(), "UserMenu is not shown"

    @allure.title("Incorect credentials sign in")
    @allure.description_html("Verifying <b>Sign in</b>page returns wearness about incorect login")
    def test_incorect_credentials_login(self, username, password):

        login_page = self.main_page.click_on_sign_up_button()
        login_page.enter_login(username).enter_password(password).click_on_login_button()

        with allure.step("Check that Forbidden text is present on the page and displayed"):
            assert login_page.forbidden_text.is_displayed(), "Forbidden is not shown"
