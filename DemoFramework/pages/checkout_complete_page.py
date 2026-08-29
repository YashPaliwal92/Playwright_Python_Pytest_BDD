from playwright.sync_api import expect

from pages.base_page import BasePage



class CheckoutCompletePage(BasePage):
    def __init__(self,page):
        super().__init__(page)

        self._success_message = page.get_by_role("heading")

    def verify_success_message(self):
        expect(self._success_message).to_contain_text("Thank you for your order!")


