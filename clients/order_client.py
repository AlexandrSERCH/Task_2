import allure

import endpoints
from clients.base_client import BaseClient
from helpers.validate_html_in_response_body import validate_html_in_response_body
from models.responses.order_response import OrderResponse, OrderResponseBody


class OrderClient:

    def __init__(self, base_client: BaseClient):
        self.base_client = base_client
        self.create_order_endpoint = endpoints.OrderEndpoints.CREATE_ORDER
        self.get_order_endpoint = endpoints.OrderEndpoints.GET_ORDER

    @allure.title("Создать заказ")
    def create_order(self, ingredients: dict, token: str = None) -> OrderResponse:
        response = self.base_client.request("POST", self.create_order_endpoint, json_body=ingredients, token=token)
        body = OrderResponseBody(**validate_html_in_response_body(response))
        return OrderResponse(status_code=response.status_code, body=body)

    @allure.title("Получить заказы")
    def get_orders(self, token: str = None) -> OrderResponse:
        response = self.base_client.request("GET", self.get_order_endpoint, token=token)
        return OrderResponse(status_code=response.status_code, body=response.json())