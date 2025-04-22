from ..test_data.user_creds import UserCredentials
from ..test_data.user_details import UserDetails


def navigate_checkout_two_page_flow(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.add_one_item_to_cart()
    cart_p = inventory_p.navigate_to_cart()
    checkout_one_p = cart_p.navigate_to_checkout_step_one_page()
    return checkout_one_p.complete_checkout_form(
        UserDetails.first_name,
        UserDetails.last_name,
        UserDetails.zip_code
    )


def test_item_is_in_cart(login_p):
    checkout_two = navigate_checkout_two_page_flow(login_p)
    assert checkout_two.is_item_present()


def test_item_is_correct(login_p):
    checkout_two = navigate_checkout_two_page_flow(login_p)
    assert checkout_two.is_item_correct()


def test_finish_purchase(login_p):
    checkout_two = navigate_checkout_two_page_flow(login_p)
    checkout_two.finish_purchase()
    assert checkout_two.is_navigate_to_checkout_complete_successful()
