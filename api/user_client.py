import endpoints
from api.base_client import BaseClient
from models.responses.user_response import UserResponse


class UserClient:

    def __init__(self, base_client: BaseClient):
        self.base_client = base_client
        self.create_user_endpoint = endpoints.UserEndpoints.CREATE_USER
        self.delete_user_endpoint = endpoints.UserEndpoints.DELETE_USER

    def create_user(self, data: dict = None) :
        response = self.base_client.post(self.create_user_endpoint, payload=data)
        return UserResponse(status_code=response.status_code, body=response.json())

    def delete_user(self, token: str = None) :
        response = self.base_client.delete(self.delete_user_endpoint, token)
        return UserResponse(status_code=response.status_code, body=response.json())
