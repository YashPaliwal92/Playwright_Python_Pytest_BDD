from pytest_bdd import scenario, given, when, then

from pages.sauce_demo import SauceDemo

@then("product should be added to cart")
def verify_product_in_cart(sauce_demo: SauceDemo, test_context):
    sauce_demo.product_page.go_to_cart()
    sauce_demo.cart_page.verify_item_in_cart(test_context['product_name'])

@when("user removes the product from cart")
def remove_product_from_cart(sauce_demo: SauceDemo, test_context):
    sauce_demo.cart_page.remove_product_from_cart(test_context['product_name'])

@then("product should be removed")
def verify_product_removed_from_cart(sauce_demo: SauceDemo, test_context):
    sauce_demo.cart_page.verify_item_removed_from_cart(test_context['product_name'])