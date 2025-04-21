def test_add_one_item_to_cart(logged):
    logged.add_one_item_to_cart()
    assert logged.is_add_item_successful()
    assert logged.is_number_of_cart_items_n('1')


def test_add_button_is_removed(logged):
    logged.add_one_item_to_cart()
    assert logged.is_add_product_button_removed()


def test_remove_button_is_present(logged):
    logged.add_one_item_to_cart()
    assert logged.is_removed_button_present()


def test_navigate_to_cart(logged):
    logged.navigate_to_cart()
    assert logged.is_navigate_to_cart_successful()
