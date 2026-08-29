from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_valid_login(app_page):
    login_page = LoginPage(app_page)

    login_page.enter_credentials("standard_user","secret_sauce")

    product_page = login_page.click_login()
    product_page.add_product_to_cart("Sauce Labs Bike Light")

    cart_page = product_page.go_to_cart()
    cart_page.verify_item_in_cart("Sauce Labs Bike Light")







