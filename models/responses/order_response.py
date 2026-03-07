from pydantic import BaseModel, Field
from typing import List


class Ingredient(BaseModel):
    id: str = Field(alias="_id")
    name: str
    type: str
    price: int


class Owner(BaseModel):
    name: str
    email: str
    createdAt: str
    updatedAt: str


class OrderData(BaseModel):
    id: str = Field(None, alias="_id")
    ingredients: List[Ingredient] = None
    owner: Owner = None
    status: str = None
    name: str = None
    number: int
    price: int = None
    createdAt: str = None
    updatedAt: str = None


class OrderItem(BaseModel):
    status: str = None
    ingredients: list = None


class OrderResponseBody(BaseModel):
    success: bool
    name: str = None
    order: OrderData = None
    orders: List[OrderItem] = None
    message: str = None


class OrderResponse(BaseModel):
    status_code: int
    body: OrderResponseBody = None
