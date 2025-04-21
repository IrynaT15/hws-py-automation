def test_complete_checkout_form(checkout_one):
    checkout_one.complete_checkout_form('FN', 'LN', '123')
    assert checkout_one.is_redirect_to_checkout_two_successful()


def test_checkout_with_missing_fn(checkout_one):
    checkout_one.complete_checkout_form('', 'LN', '123')
    assert checkout_one.error_for_missing_fn()


def test_checkout_with_missing_ln(checkout_one):
    checkout_one.complete_checkout_form('FN', '', '123')
    assert checkout_one.error_for_missing_ln()


def test_checkout_with_missing_zip(checkout_one):
    checkout_one.complete_checkout_form('FN', 'LN', '')
    assert checkout_one.error_for_missing_zip()
