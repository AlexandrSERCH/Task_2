import allure
import pytest

from data.users_data.builder_users import BuildPartialUser
from data.users_data.constans_users import EXIST_USER


@allure.epic("Пользователь")
@allure.feature("Обновление информации о пользователе")
class TestUpdateUser:

    @allure.title("Успешное обновление почты пользователе")
    def test_success_update_email_user(self, user_client, created_user):
        new_email = BuildPartialUser().with_random_email()
        result = user_client.update_user(new_email, created_user.response.body.accessToken)

        assert result.status_code == 200
        assert result.body.user.email == new_email["email"]

    @allure.title("Успешное обновление имени пользователе")
    def test_success_update_name_user(self, user_client, created_user):
        new_name = BuildPartialUser().with_random_name()
        result = user_client.update_user(new_name, created_user.response.body.accessToken)

        assert result.status_code == 200
        assert result.body.user.name == new_name["name"]

    @allure.title("Успешное обновление пароля пользователе")
    def test_success_update_password_user(self, user_client, created_user):
        new_password = BuildPartialUser().with_random_password()
        result = user_client.update_user(new_password, created_user.response.body.accessToken)

        assert result.status_code == 200
        assert result.body.success == True

    @allure.title("Ошибка валидации при обновилении информации о пользователе на существуюшую почту")
    def test_update_user_to_existing_email_returns_error(self, user_client, created_user):
        exist_email = BuildPartialUser().with_email(EXIST_USER.email)
        result = user_client.update_user(exist_email, created_user.response.body.accessToken)

        assert result.status_code == 403
        assert result.body.message == "User with such email already exists"

    user = BuildPartialUser()
    user_with_email = user.with_random_email()
    user_with_password = user.with_random_password()
    user_with_name = user.with_random_name()

    @allure.title("Ошибка валидации при попытке обновления пользователю поля '{field}', без авторизации")
    @pytest.mark.parametrize("user_data, field",
                             [(user_with_email, "email"),
                              (user_with_password, "password"),
                              (user_with_name, "name")])
    def test_update_user_without_auth_returns_error(self, user_data, field, user_client, created_user):
        result = user_client.update_user(user_data)
        assert result.status_code == 401
        assert result.body.message == "You should be authorised"
