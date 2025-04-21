def test_item_added_correctly(cart):
    assert cart.is_item_correctly_added()


def test_navigate_to_checkout_step_one(cart):
    cart.navigate_to_checkout_step_one_page()
    assert cart.is_navigate_to_checkout_step_one_successful()
