from ..helper.send_request import send_request
from ..helper.create_booking import create_booking
from ..helper.assert_json_response import assert_json_response
from ..helper.validate_response_schema import validate_response_schema


def test_successful_create_booking(read_config, read_cbt):
    response = create_booking(read_config, read_cbt["valid_data"])
    assert_json_response(read_cbt["valid_data"], response['booking'])


def test_create_booking_fails_with_missing_mandatory_data(read_config, read_cbt):
    send_request(
        "POST", f"{read_config['URL']}/booking",
        headers={
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        json=read_cbt["invalid_data"],
        status_code=500
    )


def test_create_booking_response_schema(read_config, read_cbt, read_schema):
    schema = read_schema["create booking"]
    response = create_booking(read_config, read_cbt["valid_data"])
    validate_response_schema(response, schema)
