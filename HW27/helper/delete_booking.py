import requests


def delete_booking(read_config, bookingid, auth_token):
    url = f"{read_config['URL']}/booking/{bookingid}"
    headers = {
        "Cookie": f"token={auth_token}",
    }
    response = requests.delete(url, headers=headers)
    assert response.status_code == 201, f"Wrong status code: {response.status_code}. Expected: 201"
