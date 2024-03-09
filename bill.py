from datetime import date
from person import Person
from product import Product


class Bill(object):
    def __init__(self, owner: Person, products: list[Product], bill_date: date, name: str, payment_amount: float):
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

    def print_bill(self):
        cont = 0

        print("------------------- Factura de pago -------------------")
        print(f"Compra realizada por:{self.__owner.name} \n")
        print(f"Fecha de compra: {self.__bill_date}")
        print(f"Compra realizada en: {self.__name}")
        print("------------------- Por la compra de ------------------")
        for product in self.__products:
            print(f"{product} \t\t {product.price}")
        print(f"Para un monto total de: {self.__payment_amount}")

        return
