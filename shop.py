import product
import validate
import leasable


class Shop(object):
    def __init__(self, name: str):
        self.__name = name
        self.__products = []
        self.__leasables = []
        self.__money = 0.0

    # Funciones para acceder a los atributos de la clase

    @property
    def name(self):
        return self.__name

    @property
    def products(self):
        return self.__products

    @property
    def leasable(self):
        return self.__leasables

    @property
    def money(self):
        return self.__money

    # Funciones para modificar los atributos de la clase.
    # No se necesita un modificador para la lista de productos ni rentables, pues estas varían
    # utilizando los métodos, y el setter podría resultar inefectivo.

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @money.setter
    def money(self, new_money):
        self.__money = new_money

    # Modificadores de productos
    def add_product(self, product: product):  # Función para añadir un producto a la lista
        self.__products.append(product)

    def remove_product(self, index: int):
        try:
            self.__products.pop(index - 1)
        except IndexError:
            print("El producto seleccionado no existe en la lista")

    def show_products(self):
        print("-------- Lista de productos --------")
        print("Producto \t\t precio")
        cont = 1
        for product in self.__products:
            print(f"{cont}. {product.name} \t {product.price}")
            cont += 1

    def modify_product_price(self):
        index = 0
        new = 0
        self.show_products()
        index = int(validate.validate_positive_float
                 (input("Por favor, ingrese el número asociado al producto cuyo precio desea modificar: ")))
        new = validate.validate_positive_float(input("Por favor, ingrese el nuevo valor del producto"))

        if new <= -1 or index <= -1:
            print("No ha sido posible modificar el valor del producto")
        else:
            self.__products[index - 1].price = new
            print("El valor del producto ha sido actualizado")

    # Modificadores de rentables
    def add_leasable(self, leasable: leasable):  # Función para añadir un equipo rentable a la lista
        self.__leasables.append(leasable)

    def remove_leasable(self, index: int):  # Elimina un rentable de la lista
        try:
            self.__leasables.pop(index - 1)
        except IndexError:
            print("El equipo rentable seleccionado no existe en la lista")

    def show_leasables(self):  # Imprime los rentables
        print("-------- Lista de rentables --------")
        cont = 1
        for leasable in self.__leasables:
            print(f"{cont}. {leasable.name} \t {leasable.price}")
            cont += 1

    def modify_leasable_price(self):  # Modifica un rentable de la lista
        index = 0
        new = 0
        self.show_leasables()
        index = int(validate.validate_positive_float
                    (input("Por favor, ingrese el número asociado al equipo rentable cuyo precio desea modificar: ")))
        new = validate.validate_positive_float(input("Por favor, ingrese el nuevo valor del equipo"))

        if new <= -1 or index <= -1:
            print("No ha sido posible modificar el valor del equipo rentable")
        else:
            self.__leasables[(index - 1)].price = new
            print("El valor del equipo rentable ha sido actualizado")
