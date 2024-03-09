from shop import Shop
import leasable
from datetime import date


class Debt(object):
    def __init__(self, creditor: Shop, debtor, amount, date: date):
        self.__creditor = creditor
        self.__debtor = debtor
        self.__amount = amount
        self.__date = date

    # funciones para acceder a los atributos
    @property
    def date(self):
        return self.__date

    @property
    def creditor(self):
        return self.__creditor

    @property
    def debtor(self):
        return self.__debtor

    @property
    def amount(self):
        return self.__amount

    def print_debt(self):
        print("------------------ DEUDA ---------------------")
        print("Usted debe a: ", self.creditor.name)
        print("la suma de: ", self.amount*(self.date-date.today()))
        print("----------------------------------------------")
