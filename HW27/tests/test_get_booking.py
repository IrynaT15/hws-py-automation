from ..helper.create_booking import create_booking
from ..helper.get_auth_token import get_auth_token
from ..helper.delete_booking import delete_booking
from ..helper.send_request import send_request
from ..helper.assert_json_response import assert_json_response
from ..helper.validate_response_schema import validate_response_schema


def test_successful_get_booking(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    response = send_request(
        "GET", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={"Accept": "application/json"})
    assert_json_response(read_cbt["valid_data"], response.json())


def test_get_booking_fails_for_deleted_id(read_config, read_cbt):
    booking = create_booking(read_config, read_cbt["valid_data"])
    auth_token = get_auth_token(read_config)
    delete_booking(read_config, str(booking["bookingid"]), auth_token)
    send_request(
        "GET", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={"Accept": "application/json"},
        status_code=404
    )


def test_get_booking_response_schema(read_config, read_cbt, read_schema):
    schema = read_schema["get booking"]
    booking = create_booking(read_config, read_cbt["valid_data"])
    response = send_request(
        "GET", f"{read_config['URL']}/booking/{booking['bookingid']}",
        headers={"Accept": "application/json"})
    validate_response_schema(response.json(), schema)
