import allure
import pytest

from data.orders_data.constants_orders import ORDERS_TEST_DATA, OrderData


@allure.epic("Заказы")
@allure.feature("Cоздание заказа")
class TestCreateOrder:

    @allure.title("Успешное создание: '{expected_name}', для авторизованного пользователя")
    @pytest.mark.parametrize("ingredients, expected_name", ORDERS_TEST_DATA)
    def test_success_create_order_with_auth(self, ingredients, expected_name, order_client, created_user):
        result = order_client.create_order(ingredients, created_user.response.body.accessToken)
        assert result.status_code == 200
        assert result.body.name == expected_name

    @allure.title("Успешное создание: '{expected_name}', для неавторизованного пользователя")
    @pytest.mark.parametrize("ingredients, expected_name", ORDERS_TEST_DATA)
    def test_success_create_order_with_auth(self, ingredients, expected_name, order_client, created_user):
        result = order_client.create_order(ingredients)
        assert result.status_code == 200
        assert result.body.name == expected_name

    @allure.title("Ошибка владиции при создании заказа без ингридиентов")
    def test_create_order_without_ingredients_returns_error(self, order_client):
        result = order_client.create_order({"ingredients": []})
        assert result.status_code == 400
        assert result.body.message == "Ingredient ids must be provided"

    @allure.title("Ошибка владиции при создании заказа с невалидным ингридиентом")
    def test_create_order_with_invalid_ingredients_returns_error(self, order_client):
        result = order_client.create_order({"ingredients": ["invalid_ingredient"]})
        assert result.status_code == 500
