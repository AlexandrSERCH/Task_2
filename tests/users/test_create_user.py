import allure
import pytest

from data.users_data.builder_users import BuildPartialUser


@allure.epic("Пользователь")
@allure.feature("Cоздание пользователя")
class TestCreateUser:

    @allure.title("Успешное создание пользователя")
    def test_success_create_user(self, created_user):
        assert created_user.response.status_code == 200
        assert created_user.response.body.accessToken.startswith("Bearer ")

    @allure.title("Запрет на создание дубпиката пользователя")
    def test_create_user_duplicate_returns_error(self, user_client, created_user):
        result = user_client.create_user(created_user.user_data)
        assert result.status_code == 403
        assert result.body.message == "User already exists"

    new_user = BuildPartialUser()
    user_without_email = new_user.with_password("1234").with_name("Alex")
    user_without_password = new_user.with_email("example@mail.com").with_name("Alex")
    user_without_name = new_user.with_email("example@mail.com").with_password("1234")

    @allure.title("Ошибка валидации при отсутствии обязательно поля: '{field}'")
    @pytest.mark.parametrize("user_data,field", [(user_without_email, "email"),
                                                 (user_without_password, "password"),
                                                 (user_without_name, "name")])
    def test_create_user_without_required_fields_returns_error(self, user_data, field, user_client):
        result = user_client.create_user(user_data)
        assert result.status_code == 403
        assert result.body.message == "Email, password and name are required fields"
