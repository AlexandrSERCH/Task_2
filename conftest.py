import pytest

from clients.base_client import BaseClient
from clients.user_client import UserClient
from data.users_data.builder_users import BuildUser, BuildPartialUser
from models.users.user import CreatedUser


@pytest.fixture(scope="session")
def base_client():
    return BaseClient()

@pytest.fixture(scope="session")
def user_client(base_client):
    return UserClient(base_client)

@pytest.fixture
def build_user():
    return BuildUser().build_user

@pytest.fixture
def partial_user() -> BuildPartialUser:
    return BuildPartialUser()

@pytest.fixture
def created_user(user_client, build_user):
    user_data = build_user()
    response_created_user = user_client.create_user(user_data)
    if response_created_user.status_code != 200:
        pytest.fail(f"Регистрация не прошла. Статус: {response_created_user.status_code}, тело: {response_created_user.body}")

    yield CreatedUser(response_created_user, user_data)

    deleted_user = user_client.delete_user(response_created_user.body.accessToken)
    if deleted_user.status_code != 202:
        pytest.fail(f"Удаление пользователя не прошло. Статус: {deleted_user.status_code}, тело: {deleted_user.body}")
