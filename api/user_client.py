import allure

import endpoints
from api.base_client import BaseClient
from models.responses.user_response import UserResponse


class UserClient:

    def __init__(self, base_client: BaseClient):
        self.base_client = base_client
        self.create_user_endpoint = endpoints.UserEndpoints.CREATE_USER
        self.delete_user_endpoint = endpoints.UserEndpoints.DELETE_USER

    @allure.step("Создать пользвателя")
    def create_user(self, data: dict = None) :
        response = self.base_client.request("POST", self.create_user_endpoint, json_body=data)
        return UserResponse(status_code=response.status_code, body=response.json())

    @allure.step("Удалить пользователя")
    def delete_user(self, token: str = None) :
        response = self.base_client.request("DELETE", self.delete_user_endpoint, token=token)
        return UserResponse(status_code=response.status_code, body=response.json())
