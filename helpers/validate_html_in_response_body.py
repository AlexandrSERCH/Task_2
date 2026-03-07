import requests
from requests import JSONDecodeError


def validate_html_in_response_body(response: requests.Response) -> dict:
    """Функция верхнет хардкодный словарь если на вход будет передан HTML вместо JSON"""

    try:
        body = response.json()
    except JSONDecodeError:
        body = {"success": False, "message": "В теле ответа вместо JSON находится HTML"}
    return body
