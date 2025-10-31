from decimal import Decimal

from money import Money, Wallet
from currency import rub, usd


def main():
    wallet = Wallet(money=Money(value=Decimal(150), currency=rub))
    wallet = Wallet(money=Money(value=Decimal(50), currency=usd))
    print(wallet[usd])
    print(wallet.add(money=Money(value=Decimal(1000), currency=rub)))
    print(wallet[rub])
    print(wallet.sub(money=Money(value=Decimal(200), currency=rub)))
    print(wallet[rub])
    print(len(wallet))
    del wallet[rub]
    print(wallet[rub])


if __name__ == '__main__':
    main()
