from typing import Any

payload: dict[str, Any] = {
    "name": "model-name",
    "meta": {"slug": "model-slug"},
}


class Field:

    def __init__(self, source: str):
        self.__source = source

    def __get__(self, instance, owner):
        value_payload = self.get_value_payload(
            payload=instance.payload, source=self.source
        )
        return value_payload[self.key]

    def __set__(self, instance, value):
        value_payload = self.get_value_payload(
            payload=instance.payload, source=self.source
        )
        value_payload[self.key] = value

    @property
    def source(self):
        return self.__source

    @property
    def key(self):
        return self.source.split(".")[-1]

    def get_value_payload(self, payload: dict, source: str) -> dict:
        keys = source.split(".")
        if len(keys) == 1:
            return payload
        payload.setdefault(keys[0], dict())
        if len(keys) == 2:
            return payload[keys[0]]
        return self.get_value_payload(
            payload=payload[keys[0]], source=".".join(keys[1:])
        )


class Model:

    def __init__(self, payload: dict[str, Any]):
        self.payload = payload


class User(Model):

    slug = Field("meta.slug")


user = User(payload=payload)
print(user.slug)
user.slug = "very_hard"
print(user.slug)
print(user.__dict__)
