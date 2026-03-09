import allure


@allure.epic("Заказы")
@allure.feature("Получить заказ")
class TestCreateOrder:

    @allure.title("Успешное получение заказа для авторизованного пользователя")
    def test_success_get_order(self, order_client, exists_user_with_orders):
        exist_user, test_data = exists_user_with_orders
        expected_number_orders = len(test_data)
        result = order_client.get_orders(exist_user.response.body.accessToken)

        assert result.status_code == 200
        assert len(result.body.orders) == expected_number_orders

    @allure.title("Ошибка валидации при получение заказа для неавторизованного пользователя")
    def test_get_order_without_auth_returns_errors(self, order_client):
        result = order_client.get_orders()
        assert result.status_code == 401
        assert result.body.message == "You should be authorised"
