import endpoints
from api.base_client import BaseClient
from models.responses.user_response import UserResponse


class UserClient:

    def __init__(self, base_client: BaseClient):
        self.base_client = base_client
        self.create_user_endpoint = endpoints.UserEndpoints.CREATE_USER

    def create_user(self, data: str = None) :
        response = self.base_client.post(self.create_user_endpoint, payload=data)
        return UserResponse(status_code=response.status_code, body=response.json())
