from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.cart_page import CartPage


class ProductsPage(BasePage) :

    def __init__(self,page : Page):
        super().__init__(page)

        self._products = self.page.locator(".inventory_item")
        self._cart = self.page.locator('.shopping_cart_link')

    def add_product_to_cart(self,product_name):
        product =  self._products.filter(has_text=product_name)
        product.get_by_role('button', name = 'Add to cart').click()

    def remove_product_from_cart(self, product_name):
            product = self._products.filter(has_text=product_name)
            product.get_by_role('button', name='Remove').click()

    def go_to_cart(self):
        self._cart.click()
        return CartPage(self.page)