def test_item_is_in_cart(checkout_two):
    assert checkout_two.is_item_present()


def test_item_is_correct(checkout_two):
    assert checkout_two.is_item_correct()


def test_finish_purchase(checkout_two):
    checkout_two.finish_purchase()
    assert checkout_two.is_navigate_to_checkout_complete_successful()
