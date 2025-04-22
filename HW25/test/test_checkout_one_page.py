from ..test_data.user_creds import UserCredentials
from ..test_data.user_details import UserDetails


def navigate_checkout_one_page_flow(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.add_one_item_to_cart()
    cart_p = inventory_p.navigate_to_cart()
    return cart_p.navigate_to_checkout_step_one_page()


def test_complete_checkout_form(login_p):
    checkout_one = navigate_checkout_one_page_flow(login_p)
    checkout_one.complete_checkout_form(
        UserDetails.first_name,
        UserDetails.last_name,
        UserDetails.zip_code
    )
    assert checkout_one.is_redirect_to_checkout_two_successful()


def test_checkout_with_missing_fn(login_p):
    checkout_one = navigate_checkout_one_page_flow(login_p)
    checkout_one.complete_checkout_form(
        UserDetails.empty_fn,
        UserDetails.last_name,
        UserDetails.zip_code
    )
    assert checkout_one.error_for_missing_fn()


def test_checkout_with_missing_ln(login_p):
    checkout_one = navigate_checkout_one_page_flow(login_p)
    checkout_one.complete_checkout_form(
        UserDetails.first_name,
        UserDetails.empty_ln,
        UserDetails.zip_code
    )
    assert checkout_one.error_for_missing_ln()


def test_checkout_with_missing_zip(login_p):
    checkout_one = navigate_checkout_one_page_flow(login_p)
    checkout_one.complete_checkout_form(
        UserDetails.first_name,
        UserDetails.last_name,
        UserDetails.empty_zip
    )
    assert checkout_one.error_for_missing_zip()
