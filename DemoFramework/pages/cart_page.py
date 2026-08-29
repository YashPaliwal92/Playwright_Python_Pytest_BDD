from playwright.sync_api import Page, expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def __init__(self, page : Page):
        super().__init__(page)

        self._cart_items = page.locator(".cart_list")
        self._checkout_button = page.get_by_role('button' , name = 'Checkout')
        self._continue_shopping_button  = page.get_by_role('button' , name = 'Continue Shopping')

    def checkout(self):
        self._checkout_button.click()

    def continue_shopping(self):
        self._continue_shopping_button.click()

    def verify_item_in_cart(self, product_name):
        expect(self._cart_items).to_contain_text(product_name)

    def remove_product_from_cart(self, product_name):
        product = self._cart_items.filter(has_text=product_name)
        product.get_by_role('button', name='Remove').click()

    def verify_item_removed_from_cart(self, product_name):
            expect(self._cart_items).not_to_contain_text(product_name)
