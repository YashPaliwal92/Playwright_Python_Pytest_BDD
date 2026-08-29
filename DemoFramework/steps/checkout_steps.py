from pytest_bdd import scenario, given, when, then, parsers

from pages.sauce_demo import SauceDemo

@when("user fills following details to checkout")
def fill_details_to_checkout(sauce_demo: SauceDemo, datatable):
    first_name, last_name, zip_code = datatable[1]
    sauce_demo.cart_page.checkout()
    sauce_demo.checkout_page.enter_checkout_details(first_name, last_name, zip_code)
    sauce_demo.checkout_page.click_continue()

@then("user reviews the product detail")
def review_the_product_before_final_checkout(sauce_demo: SauceDemo, test_context):
    sauce_demo.checkout_overview_page.verify_checkout_item(test_context['product_name'])

@when("user finishes checking out")
def finish_checkout(sauce_demo: SauceDemo):
    sauce_demo.checkout_overview_page.click_finish()

@then("user should successfully buy the product")
def successfully_buy_product(sauce_demo: SauceDemo):
    sauce_demo.checkout_complete_page.verify_success_message()






