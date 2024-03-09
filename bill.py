from datetime import date
import user


class Bill(object):
    def __init__(self, owner: user, products, bill_date: date, name: str, payment_amount: float):
        self.__owner = owner
        self.__products = products
        self.__payment_amount = payment_amount
        self.__bill_date = bill_date
        self.__name = name
        self.__payment_amount = payment_amount

    @property
    def owner(self):
        return self.__owner

    @property
    def products(self):
        return self.__products

    @property
    def payment_amount(self):
        return self.__payment_amount

    @property
    def bill_date(self):
        return self.__bill_date
