from ..helper.create_booking import create_booking
from ..helper.get_auth_token import get_auth_token
from ..helper.send_request import send_request
from ..helper.assert_json_response import assert_json_response
from ..helper.validate_response_schema import validate_response_schema


def test_successful_update_booking(read_config, read_cbt, read_ubt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    url = f"{read_config['URL']}/booking/{booking['bookingid']}"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        "Cookie": f"token={auth_token}"
    }
    put_response = send_request("PUT", url, headers=headers, json=read_ubt["valid_template"])
    assert_json_response(read_ubt["valid_template"], put_response.json())

    get_response = send_request("GET", url, headers=headers)
    assert_json_response(read_ubt["valid_template"], get_response.json())


def test_update_fails_with_totalprice_none(read_config, read_cbt, read_ubt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    send_request(
        "PUT", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={'Content-Type': 'application/json', 'Accept': 'application/json', "Cookie": f"token={auth_token}"},
        json=read_ubt["totalprice null"],
        status_code=400
    )


def test_update_booking_response_schema(read_config, read_cbt, read_schema, read_ubt):
    schema = read_schema["update booking"]
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    response = send_request(
        "PUT", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={'Content-Type': 'application/json', 'Accept': 'application/json', "Cookie": f"token={auth_token}"},
        json=read_ubt["valid_template"]
    )
    validate_response_schema(response.json(), schema)
