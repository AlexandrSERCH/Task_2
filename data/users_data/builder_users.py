from faker import Faker

fake = Faker("ru_RU")

class BuildUser:

    @staticmethod
    def build_user(*, email: str | None = None, password: str | None = None, name: str | None = None) -> dict:
        """Если не заполнить именнованные аргументы, то поля заполнятся фейковыми данными"""

        return {
            "email": email if email else fake.email(),
            "password": password if password else fake.password(length=8, special_chars=False),
            "name": name if name else fake.first_name()
        }

class BuildPartialUser(dict):

    def _set(self, key: str, value) -> BuildPartialUser:
        clone = BuildPartialUser(self) # создаём копию текущего состояния, чтобы не мутировать оригинал
        clone[key] = value
        return clone

    def with_email(self, email: str) -> BuildPartialUser:
        return self._set("email", email)

    def with_random_email(self):
        return self._set("email", fake.email())

    def with_password(self, password: str) -> BuildPartialUser:
        return self._set("password", password)

    def with_random_password(self):
        return self._set("password", fake.password(length=8, special_chars=False))

    def with_name(self, name: str) -> BuildPartialUser:
        return self._set("name", name)