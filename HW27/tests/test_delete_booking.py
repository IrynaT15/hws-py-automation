from ..helper.send_request import send_request
from ..helper.create_booking import create_booking
from ..helper.get_auth_token import get_auth_token
from ..helper.delete_booking import delete_booking


def test_successful_delete_booking(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    delete_booking(read_config, str(booking["bookingid"]), auth_token)


def test_delete_booking_fails_for_not_authorized_user(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    url = f"{read_config['URL']}/booking/{booking['bookingid']}"
    send_request("DELETE", url, status_code=403)


def test_delete_booking_fails_for_already_deleted_id(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    url = f"{read_config['URL']}/booking/{booking['bookingid']}"
    headers = {
        "Cookie": f"token={auth_token}",
    }
    send_request("DELETE", url, headers=headers, status_code=201)
    send_request("DELETE", url, headers=headers, status_code=405)
