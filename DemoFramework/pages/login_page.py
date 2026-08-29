from playwright.sync_api import Page, expect

from pages.base_page import BasePage
from pages.products_page import ProductsPage


class LoginPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self._username_input = self.page.get_by_placeholder("Username")
        self._password_input = self.page.get_by_placeholder("Password")
        self._login_button = self.page.get_by_role('button', name = 'Login')
        self._login_error = self.page.locator('.error-message-container.error')

    def enter_credentials(self, username, password):
        self._username_input.fill(username)
        self._password_input.fill(password)

    def click_login(self):
        self._login_button.click()
        return ProductsPage(self.page)

    def verify_url_after_login(self):
        assert "inventory" in self.get_url()

    def verify_locked_user_error(self):
            expect(self._login_error).to_contain_text("Sorry, this user has been locked out")

    def verify_invalid_user_error(self):
            expect(self._login_error).to_contain_text("Username and password do not match any user in this service")
