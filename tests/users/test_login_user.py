import allure
import pytest

from data.users_data.builder_users import BuildPartialUser
from data.users_data.constans_users import EXIST_USER


@allure.epic("Пользователь")
@allure.feature("Авторизация пользователя")
class TestLoginUser:

    @allure.title("Успешная авторизация пользователя")
    def test_success_login_user(self, user_client, created_user):
        login_payload = {
            "email": created_user.user_data["email"],
            "password": created_user.user_data["password"]
        }
        result = user_client.login_user(login_payload)

        assert result.status_code == 200
        assert result.body.accessToken.startswith("Bearer ")

    new_user = BuildPartialUser()
    user_with_invalid_login = new_user.with_email("invalid_email@mail.com").with_password(EXIST_USER.password)
    user_with_invalid_password = new_user.with_email(EXIST_USER.email).with_password("Inval1d_pa$sword")
    user_with_invalid_login_and_password = new_user.with_email('invalid_email_2@mail.com').with_password("Inval1d_pa$sword2")

    @allure.title("Ошибка валидации c неверном полем: '{field}'")
    @pytest.mark.parametrize("user_data, field", [
        (user_with_invalid_login, "логин"),
        (user_with_invalid_password, "пароль"),
        (user_with_invalid_login_and_password, "логин и пароль")])
    def test_login_user_with_invalid_login_or_password_returns_error(self, user_data, field, user_client):
        result = user_client.login_user(user_data)
        assert result.status_code == 401
        assert result.body.message == "email or password are incorrect"