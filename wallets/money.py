from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, Self

from currency import Currency
from exceptions import SameValueException, NegativeValueException


@dataclass(frozen=True, slots=True)
class Money:
    value: Decimal
    currency: Currency

    def __add__(self, other):
        self.check_current_currency(other=other)
        return Money(value=self.value + other.value, currency=self.currency)

    def __sub__(self, other):
        return Money(value=self.value - other.value, currency=self.currency)

    def check_current_currency(self, other):
        if not self.currency == other.currency:
            raise SameValueException('Валюта должна быть одинаковой!')

    def negative_value(self):
        return self.value < 0


class Wallet:

    def __init__(self, money: Money):
        self.__balance: Dict[str, Money] = {}
        self.add(money)

    def __getitem__(self, item: Currency):
        return self.__balance.setdefault(item, Money(value=Decimal(0), currency=item))

    def __setitem__(self, key: Currency, value: Money):
        if key != value.currency:
            raise SameValueException(
                f'Ключ {key} и валюта {value.currency} не совпадают!'
            )
        self.__balance[key] = value

    def __delitem__(self, key: Currency):
        if key in self:
            del self.__balance[key]

    def __contains__(self, item: Currency):
        return item in self.currencies

    def __len__(self):
        return len(self.currencies)

    @property
    def currencies(self):
        return self.__balance.keys()

    def add(self, money: Money) -> Self:
        self[money.currency] = self[money.currency] + money
        return self

    def sub(self, money: Money) -> Self:
        new_balance = self[money.currency] - money
        if new_balance.negative_value():
            raise NegativeValueException('Недостачно средст для списания!')
        self[money.currency] = new_balance
        return self
