from playwright.sync_api import expect

from pages.base_page import BasePage



class CheckoutOverviewPage(BasePage):
    def __init__(self,page):
        super().__init__(page)

        self._cart_items = page.locator(".cart_item")
        self._finish_button = page.get_by_role('button', name = 'Finish')

    def verify_checkout_item(self, product_name):
        expect(self._cart_items).to_contain_text(product_name)

    def click_finish(self):
        self._finish_button.click()


