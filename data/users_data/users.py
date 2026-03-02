from dataclasses import dataclass


@dataclass
class UserData:
    email: str
    password: str
    name: str

EXISTS_USER = UserData(
    email="alex_29@mail.com",
    password="123456qA",
    name="Alexnadr",
)