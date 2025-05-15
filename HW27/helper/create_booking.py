import requests


def create_booking(read_config, payload):
    url = f"{read_config['URL']}/booking"
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    response = requests.post(url, headers=headers, json=payload)
    assert response.status_code == 200, f"Wrong status code: {response.status_code}. Expected: 200"
    return response.json()
