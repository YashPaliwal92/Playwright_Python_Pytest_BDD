from pytest_bdd import scenario, given, when, then, parsers

from pages.sauce_demo import SauceDemo

@when(parsers.parse("user selects the product '{product_name}'"))
def select_product(sauce_demo: SauceDemo, product_name : str, test_context):
    test_context['product_name'] = product_name
    sauce_demo.product_page.add_product_to_cart(product_name)
