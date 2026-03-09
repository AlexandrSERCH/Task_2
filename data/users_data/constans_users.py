from pydantic import BaseModel

class UserData(BaseModel):
    email: str
    password: str
    name: str

EXIST_USER = UserData(
    email="alex_29@mail.com",
    password="123456qA",
    name="Alexnadr",
)