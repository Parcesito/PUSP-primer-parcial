class Product(object):
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    # Funciones para acceder a las propiedades del objeto
    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    # Funciones para modificar las propiedades del objeto
    @price.setter
    def price(self, price: float):
        self.__price = price

    @name.setter
    def name(self, name: str):
        self.__name = name
