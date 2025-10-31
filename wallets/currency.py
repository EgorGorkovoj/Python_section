import enum
from dataclasses import dataclass


class AvailableCurrency(enum.StrEnum):
    RUB = enum.auto()
    USD = enum.auto()


@dataclass(slots=True, frozen=True)
class Currency:
    code: AvailableCurrency


@dataclass(slots=True, frozen=True)
class RUB(Currency):
    code: AvailableCurrency = AvailableCurrency.RUB


@dataclass(slots=True, frozen=True)
class USD(Currency):
    code: AvailableCurrency = AvailableCurrency.USD


rub = RUB()
usd = USD()
