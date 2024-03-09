
class Leasable(object):
    def __init__(self, name: str, price: float, damage: bool):
        self.__name = name
        self.__price = price  # Precio por día de alquiler
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def rented(self):
        return self.__rented

    @property
    def price(self) -> float:
        return self.__price

    @property
    def damage(self) -> bool:
        return self.__damage

    @damage.setter
    def damage(self, damage: bool):
        self.__damage = damage

    @price.setter
    def price(self, price: float):
        self.__price = price

    @name.setter
    def name(self, name: str):
        self.__name = name

    @rented.setter
    def rented(self, rented: bool):
        self.__rented = rented
