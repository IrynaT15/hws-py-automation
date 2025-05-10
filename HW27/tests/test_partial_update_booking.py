from ..helper.create_booking import create_booking
from ..helper.get_auth_token import get_auth_token
from ..helper.send_request import send_request
from ..helper.assert_json_response import assert_json_response


def test_successful_patch_update_fn_ln(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)

    url = f"{read_config['URL']}/booking/{booking['bookingid']}"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Cookie": f"token={auth_token}"
    }
    payload = {
        "firstname": "James",
        "lastname": "Brown"
    }

    response = send_request("PATCH", url, headers=headers, json=payload)
    assert response.json()['firstname'] == payload['firstname']
    assert response.json()['lastname'] == payload['lastname']

    new_valid_data = read_cbt["valid_data"].copy()
    new_valid_data['firstname'] = payload['firstname']
    new_valid_data['lastname'] = payload['lastname']

    response = send_request("GET", url, headers=headers)
    assert_json_response(new_valid_data, response.json())


def test_patch_update_fails_for_not_authorized_user(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    send_request(
        "PATCH", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={"Content-Type": "application/json", "Accept": "application/json"},
        json={"firstname": "James", "lastname": "Brown"},
        status_code=403
    )
