from pytest_bdd import scenario, given, when, then, parsers

from pages.sauce_demo import SauceDemo

@given("a valid user logs in")
def user_login(sauce_demo : SauceDemo, config_data):
    username, password = config_data.get_credential()
    sauce_demo.login_page.enter_credentials(username, password)
    sauce_demo.login_page.click_login()

@then("user should login successfully")
def login_validation(sauce_demo : SauceDemo):
    sauce_demo.login_page.verify_url_after_login()

@given("a locked user tries to login")
def locked_user_login(sauce_demo : SauceDemo, config_data):
    username, password = config_data.get_locked_user()
    sauce_demo.login_page.enter_credentials(username, password)
    sauce_demo.login_page.click_login()

@then("locked user should not be allowed to login")
def validate_locked_user_error(sauce_demo : SauceDemo):
    sauce_demo.login_page.verify_locked_user_error()

@given("an invalid user tries to login")
def invalid_user_login(sauce_demo : SauceDemo, config_data):
    username, password = config_data.get_invalid_user()
    sauce_demo.login_page.enter_credentials(username, password)
    sauce_demo.login_page.click_login()

@then("invalid user should not be allowed to login")
def validate_invalid_user_error(sauce_demo : SauceDemo):
    sauce_demo.login_page.verify_invalid_user_error()