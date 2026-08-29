from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def __init__(self,page):
        super().__init__(page)

        self._first_name_input = page.get_by_placeholder("First Name")
        self._last_name_input = page.get_by_placeholder("Last Name")
        self._zip_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role('button', name = 'Continue')

    def enter_checkout_details(self,first_name,last_name,zip_code):
        self._first_name_input.fill(first_name)
        self._last_name_input.fill(last_name)
        self._zip_code_input.fill(zip_code)

    def click_continue(self):
        self.continue_button.click()


