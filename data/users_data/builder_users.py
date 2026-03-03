from faker import Faker


class BuildUser:

    @staticmethod
    def build_user(*, email: str | None = None, password: str | None = None, name: str | None = None) -> dict:
        """Если не заполнить именнованные аргументы, то поля заполнятся фейковыми данными"""

        fake = Faker("ru_RU")

        return {
            "email": email if email else fake.email(),
            "password": password if password else fake.password(length=8, special_chars=False),
            "name": name if name else fake.first_name()
        }

class BuildPartialUser(dict):

    def with_email(self, email: str) -> BuildPartialUser:
        self["email"] = email
        return self

    def with_password(self, password: str) -> BuildPartialUser:
        self["password"] = password
        return self

    def with_name(self, name: str) -> BuildPartialUser:
        self["name"] = name
        return self