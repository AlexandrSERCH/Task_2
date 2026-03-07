from typing import NamedTuple


class OrderData(NamedTuple):
    payload: dict
    expected_name: str


ORDERS_TEST_DATA = [
    OrderData(
        payload={
            "ingredients": [
                "61c0c5a71d1f82001bdaaa6c",
            ]
        },
        expected_name="Краторный бургер"
    ),
    OrderData(
        payload={
            "ingredients": [
                "61c0c5a71d1f82001bdaaa76",
                "61c0c5a71d1f82001bdaaa6c",
            ]
        },
        expected_name="Минеральный краторный бургер"
    ),
    OrderData(
        payload={
            "ingredients": [
                "61c0c5a71d1f82001bdaaa72",
                "61c0c5a71d1f82001bdaaa75",
                "61c0c5a71d1f82001bdaaa6e",
                "61c0c5a71d1f82001bdaaa6d",
            ]
        },
        expected_name="Люминесцентный флюоресцентный spicy антарианский бургер"
    ),
]
