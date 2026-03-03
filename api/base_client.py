import requests

from config import BASE_URL


class BaseClient:

    def __init__(self, token: str = None):
        self.BASE_URL = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def get(self, endpoint: str, params: str = None) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}{endpoint}", params=params)

    def post(self, endpoint: str, payload: dict = None) -> requests.Response:
        return self.session.post(f"{self.BASE_URL}{endpoint}", json=payload)

    def delete(self, endpoint: str, token: str) -> requests.Response:
        if token:
            self.session.headers.update({"Authorization": f"{token}"})

        return self.session.delete(f"{self.BASE_URL}{endpoint}")

