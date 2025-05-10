import json
import pytest


@pytest.fixture
def read_config():
    with open("HW27/test_data/config.json") as f:
        return json.load(f)


@pytest.fixture
def read_cbt():
    with open("HW27/test_data/create_booking_template.json") as f:
        return json.load(f)


@pytest.fixture
def read_schema():
    with open("HW27/test_data/response_schemas.json") as f:
        return json.load(f)


@pytest.fixture
def read_ubt():
    with open("HW27/test_data/update_booking_template.json") as f:
        return json.load(f)
