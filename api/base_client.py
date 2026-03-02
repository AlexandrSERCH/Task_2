import requests

from config import BASE_URL


class BaseClient:

    def __init__(self, token: str = None):
        self.BASE_URL = BASE_URL
        self.session = requests.Session()
        # self.token = token
        #
        # if token:
        #     self.session.headers.update({
        #         "Authorization": f"Bearer {token}",
        #         "Content-Type": "application/json"
        #     })

    def get(self, endpoint: str, payload: dict = None) -> requests.Response:
        return self.session.get(f"{self.BASE_URL}{endpoint}", data=payload)

    def post(self, endpoint: str, payload: dict = None) -> requests.Response:
        return self.session.post(f"{self.BASE_URL}{endpoint}", data=payload)

