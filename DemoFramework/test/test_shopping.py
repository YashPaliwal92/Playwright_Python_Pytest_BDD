from pytest_bdd import scenarios

from steps.cart_steps import *
from steps.checkout_steps import *
from steps.product_steps import *
from steps.login_steps import *

scenarios(
    '../features/login.feature',
    '../features/shopping.feature'
)
