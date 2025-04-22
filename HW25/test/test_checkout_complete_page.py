from ..test_data.user_creds import UserCredentials
from ..test_data.user_details import UserDetails


def navigate_complete_page_flow(login_p):
    inventory_p = login_p.complete_login(UserCredentials.standard_user, UserCredentials.valid_password)
    inventory_p.add_one_item_to_cart()
    cart_p = inventory_p.navigate_to_cart()
    checkout_one_p = cart_p.navigate_to_checkout_step_one_page()
    checkout_two_p = checkout_one_p.complete_checkout_form(
        UserDetails.first_name,
        UserDetails.last_name,
        UserDetails.zip_code
    )
    return checkout_two_p.finish_purchase()


def test_complete_header_text(login_p):
    complete = navigate_complete_page_flow(login_p)
    assert complete.is_complete_header_text_correct()


def test_back_home(login_p):
    complete = navigate_complete_page_flow(login_p)
    assert complete.back_home()
