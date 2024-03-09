import person
import shop


class debt(object):
    def __init__(self, creditor: shop, debtor: person, amount):
        self.__creditor = creditor
        self.__debtor = debtor
        self.__amount = amount

    # funciones para acceder a los atributos
    @property
    def creditor(self):
        return self.__creditor

    @property
    def debtor(self):
        return self.__debtor

    @property
    def amount(self):
        return self.__amount
