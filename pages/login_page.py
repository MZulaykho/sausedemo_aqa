from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.user_name = self.page.locator("#user-name")
        self.password = self.page.locator("#password")
        self.button_login = self.page.locator("#login-button")

    def fill_user_name(self, login):
        self.user_name.fill(login)

    def expect_user_name(self, value):
        expect(self.user_name).to_have_value(value)

    def fill_password(self, password):
        self.password.fill(password)

    def expect_password(self, value):
        expect(self.password).to_have_value(value)

    def click_button_login(self):
        self.button_login.click()