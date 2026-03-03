import pytest

from data.users_data.builder_users import BuildPartialUser


class TestCreateUser:

    def test_success_create_user(self, created_user):
        assert created_user.response.status_code == 200
        assert created_user.response.body.accessToken.startswith("Bearer ")

    def test_create_user_duplicate_returns_error(self, user_client, created_user):
        result = user_client.create_user(created_user.user_data)
        assert result.status_code == 403
        assert result.body.message == "User already exists"


    @pytest.mark.parametrize("user_data", [
        pytest.param(
            BuildPartialUser().with_email("example@mail.com").with_password("1234"),
            id="Остутствует обязательное поле 'name'"
),
        pytest.param(
            BuildPartialUser().with_email("example@mail.com").with_name("Alex"),
            id="Остутствует обязательное поле 'password'"
        ),
        pytest.param(
            BuildPartialUser().with_password("1234").with_name("Alex"),
            id="Остутствует обязательное поле 'email'"
        )
    ])
    def test_create_user_without_required_fields_returns_error(self, user_data, user_client):
        result = user_client.create_user(user_data)
        assert result.status_code == 403
        assert result.body.message == "Email, password and name are required fields"
