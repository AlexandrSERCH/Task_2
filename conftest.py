import pytest

from api.base_client import BaseClient
from api.user_client import UserClient


@pytest.fixture(scope="session")
def base_client():
    return BaseClient()

@pytest.fixture(scope="session")
def user_client(base_client):
    return UserClient(base_client)