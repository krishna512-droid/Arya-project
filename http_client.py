import requests

def get_json(url, params=None, timeout=10):
    response = requests.get(
        url,
        params=params,
        timeout=timeout,
        headers={"User-Agent": "PS10-Hackathon-Demo/1.0"}
    )
    response.raise_for_status()
    return response.json()
