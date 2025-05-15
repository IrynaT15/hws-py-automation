import requests


def get_auth_token(read_config):
    url = f"{read_config['URL']}/auth"
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        "username": "admin",
        "password": "password123"
    }
    auth_token = requests.post(url, headers=headers, json=payload)
    return auth_token.json()["token"]
