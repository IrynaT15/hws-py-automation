from ..test_data.user_creds import UserCredentials


def navigate_cart_page_flow(login_p):
    inventory_p = login_p.complete_login(UserCredentials.standard_user, UserCredentials.valid_password)
    inventory_p.add_one_item_to_cart()
    return inventory_p.navigate_to_cart()


def test_item_added_correctly(login_p):
    cart_p = navigate_cart_page_flow(login_p)
    assert cart_p.is_item_correctly_added()


def test_navigate_to_checkout_step_one(login_p):
    cart_p = navigate_cart_page_flow(login_p)
    cart_p.navigate_to_checkout_step_one_page()
    assert cart_p.is_navigate_to_checkout_step_one_successful()
