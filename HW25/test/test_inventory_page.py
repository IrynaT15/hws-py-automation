from ..test_data.user_creds import UserCredentials


def test_add_one_item_to_cart(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.add_one_item_to_cart()
    assert inventory_p.is_add_item_successful()
    assert inventory_p.is_number_of_cart_items_n('1')


def test_add_button_is_removed(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.add_one_item_to_cart()
    assert inventory_p.is_add_product_button_removed()


def test_remove_button_is_present(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.add_one_item_to_cart()
    assert inventory_p.is_removed_button_present()


def test_navigate_to_cart(login_p):
    inventory_p = login_p.complete_login(
        UserCredentials.standard_user,
        UserCredentials.valid_password
    )
    inventory_p.navigate_to_cart()
    assert inventory_p.is_navigate_to_cart_successful()
