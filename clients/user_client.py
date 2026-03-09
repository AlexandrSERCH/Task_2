import allure

import endpoints
from clients.base_client import BaseClient
from models.responses.user_response import UserResponse


class UserClient:

    def __init__(self, base_client: BaseClient):
        self.base_client = base_client
        self.create_user_endpoint = endpoints.UserEndpoints.CREATE_USER
        self.delete_user_endpoint = endpoints.UserEndpoints.DELETE_USER
        self.login_user_endpoint = endpoints.UserEndpoints.LOGIN_USER
        self.update_user_endpoint = endpoints.UserEndpoints.UPDATE_USER

    @allure.step("Создать пользвателя")
    def create_user(self, data: dict = None) -> UserResponse:
        response = self.base_client.request("POST", self.create_user_endpoint, json_body=data)
        return UserResponse(status_code=response.status_code, body=response.json())

    @allure.step("Удалить пользователя")
    def delete_user(self, token: str = None) -> UserResponse:
        response = self.base_client.request("DELETE", self.delete_user_endpoint, token=token)
        return UserResponse(status_code=response.status_code, body=response.json())

    @allure.step("Авторизоваться")
    def login_user(self, data: dict) -> UserResponse:
        response = self.base_client.request("POST", self.login_user_endpoint, json_body=data)
        return UserResponse(status_code=response.status_code, body=response.json())

    def update_user(self, data: dict =  None, token: str = None):
        response = self.base_client.request("PATCH", self.update_user_endpoint, json_body=data, token=token)
        return UserResponse(status_code=response.status_code, body=response.json())
