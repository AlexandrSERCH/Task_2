import json
import time

import allure
import requests

from config import BASE_URL
from helpers.build_curl import build_curl


class BaseClient:

    def __init__(self):
        self.BASE_URL = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({"Content-Type": "application/json"})

    def request(self,
                 method: str,
                 endpoint: str,
                 *,
                 json_body: dict = None,
                 params: str = None,
                 token: str = None) -> requests.Response:

        url = f"{self.BASE_URL}{endpoint}"
        merged_headers = dict(self.session.headers) | ({"Authorization": f"{token}"} if token else {})
        curl = build_curl(method, url, merged_headers, json_body)

        with allure.step(f"{method.upper()} {endpoint}"):
            allure.attach(url, "url", allure.attachment_type.TEXT)
            allure.attach(curl, "cURL", allure.attachment_type.TEXT)
            if params:
                allure.attach(json.dumps(params, ensure_ascii=False, indent=2), "params", allure.attachment_type.JSON)
            if merged_headers:
                allure.attach(json.dumps(merged_headers, ensure_ascii=False, indent=2), "headers", allure.attachment_type.JSON)
            if json_body:
                allure.attach(json.dumps(json_body, ensure_ascii=False, indent=2), "request_body", allure.attachment_type.JSON)

        start_time = time.time()

        response = self.session.request(
            method=method.upper(),
            url=url,
            json=json_body,
            params=params,
            headers=merged_headers)

        response_time = f"{time.time() - start_time:.2f}"

        allure.attach(str(response.status_code), "response_status_code", allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(response.headers), ensure_ascii=False, indent=2), "response_headers", allure.attachment_type.JSON)
        allure.attach(response.text, "response_body", allure.attachment_type.TEXT)
        allure.attach(response_time, "response_time_in_sec", allure.attachment_type.TEXT)

        return response



