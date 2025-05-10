import requests


def send_request(method, url, headers=None, params=None, data=None, json=None, status_code=200):
    response = requests.request(method, url, headers=headers, params=params, data=data, json=json)
    assert response.status_code == status_code, f"Wrong status code: {response.status_code}. Expected: {status_code}"
    return response
