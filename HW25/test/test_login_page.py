import pytest
from ..test_data.user_creds import UserCredentials


def test_login_w_valid_creds(login_p):
    login_p.complete_login(UserCredentials.standard_user, UserCredentials.valid_password)
    assert login_p.is_login_successful()


@pytest.mark.parametrize('username, password', [
    ('test', UserCredentials.valid_password),
    (UserCredentials.standard_user, 'test'),
])
def test_login_w_invalid_creds(login_p, username, password):
    login_p.complete_login(username, password)
    assert login_p.is_login_page()
    assert login_p.is_error_present()
    assert login_p.is_error_for_invalid_creds()


@pytest.mark.parametrize('username, password', [
    ('', UserCredentials.valid_password),
    ('', ''),
])
def test_login_w_missing_username(login_p, username, password):
    login_p.complete_login(username, password)
    assert login_p.is_login_page()
    assert login_p.is_error_present()
    assert login_p.is_error_for_missing_username()


def test_login_w_missing_password(login_p):
    login_p.complete_login(UserCredentials.valid_password, '')
    assert login_p.is_login_page()
    assert login_p.is_error_present()
    assert login_p.is_error_for_missing_password()


def test_login_w_locked_user(login_p):
    login_p.complete_login(UserCredentials.locked_out_user, UserCredentials.valid_password)
    assert login_p.is_login_page()
    assert login_p.is_error_present()
    assert login_p.is_error_for_locked_user()
