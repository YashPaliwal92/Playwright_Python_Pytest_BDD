from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


class SauceDemo:
    def __init__(self,app_page):
        self.login_page = LoginPage(app_page)
        self.product_page = ProductsPage(app_page)
        self.cart_page = CartPage(app_page)
        self.checkout_page = CheckoutPage(app_page)
        self.checkout_overview_page = CheckoutOverviewPage(app_page)
        self.checkout_complete_page = CheckoutCompletePage(app_page)