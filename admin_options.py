import person
from person import Person
from leasable import Leasable
import shop
from product import Product
from shop import Shop
import time
import os
import validate


def create_shop(shops: list[shop]):
    print("--------------- Crear establecimiento ---------------")
    name: str
    name = input("Por favor, ingrese el nombre del nuevo establecimiento: ")
    shops.append(Shop(name))
    print(f"¡El establecimiento {name} ha sido creado, felicitaciones!")
    print("------------------------------------------------------")
    time.sleep(2)
    os.system("cls")


def show_shops(shops: list[shop]):
    print("--------------- Establecimientos disponibles ---------------")
    cont = 1
    for shop in shops:
        print(f"{cont}. {shop.name}")
        cont += 1
    print("------------------------------------------------------------")

def delete_shop(shops: list):
    index = 0
    aux = 0
    show_shops(shops)
    index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado con el establecimiento"
                                                       "a eliminar: ")))
    time.sleep(1)
    os.system("cls")
    try:
        aux = shops[index - 1]
    except IndexError:
        print("------------------------------------------------------")
        print("       No se ha encontrado el establecimiento")
        print("                       solicitado.")
        print("------------------------------------------------------")
        time.sleep(1)
        print("------------------------------------------------------")
        print("                  Regresando al menú")
        print("                       Principal")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return
    else:
        shops.pop(index-1)
        print("------------------------------------------------------")
        print("          El establecimiento ha sido eliminado")
        print("                       exitosamente")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return

def modify_shop(shops: list):
    index = 0
    aux = 0
    show_shops(shops)
    index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado con el establecimiento"
                                                       "a modificar: ")))
    time.sleep(1)
    os.system("cls")
    try:
        aux = shops[index - 1]
    except IndexError:
        print("------------------------------------------------------")
        print("       No se ha encontrado el establecimiento")
        print("                       solicitado.")
        print("------------------------------------------------------")
        time.sleep(1)
        print("------------------------------------------------------")
        print("                  Regresando al menú")
        print("                       Principal")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return
    else:
        print(f"--------------- Estado de {aux.name} ---------------")
        print("1 - Añadir producto.")
        print("2 - Eliminar producto.")
        print("3 - Modificar precio de producto")
        print("4 - Añadir equipo rentable")
        print("5 - Eliminar equipo rentable")
        print("6 - Modificar precio de equipo rentable")
        print("7 - Volver al menú principal")
        print("------------------------------------------------------")
        # Se reutiliza la variable index
        index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado con la acción"
                                                           "deseada: ")))
        time.sleep(1)
        os.system("cls")

        if index == 1:
            price = 0
            print("------------------------------------------------------")
            name = input("Por favor, ingrese el nombre del nuevo producto: ")
            while price == 0:
                price = validate.validate_positive_float(input("Por favor, ingrese el valor del nuevo producto: "))
            aux.add_product(Product(name, price))
            print("El producto ha sido añadido correctamente.")
            print("------------------------------------------------------")
            time.sleep(2)
            os.system("cls")
            return

        elif index == 2:
            aux.show_products()
            print("------------------------------------------------------")
            index = int(
                validate.validate_positive_float(input("Por favor, ingrese el número relacionado con el producto"
                                                       "a eliminar: ")))
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            try:
                aux2 = aux.products[index - 1]
            except IndexError:
                print("------------------------------------------------------")
                print("            No se ha encontrado el producto")
                print("                       solicitado.")
                print("------------------------------------------------------")
                time.sleep(2)
                os.system("cls")
                return
            else:
                aux.remove_product(index - 1)
                print("El producto ha sido eliminado satisfactoriamente.")
                time.sleep(2)
                os.system("cls")
                return

        elif index == 3:
            print("------------------------------------------------------")
            aux.modify_product_price()
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            return

        elif index == 4:
            price = 0
            print("------------------------------------------------------")
            name = input("Por favor, ingrese el nombre del nuevo equipo rentable: ")
            while price == 0:
                price = validate.validate_positive_float(
                    input("Por favor, ingrese el valor del nuevo equipo rentable: "))
            aux.add_leasable(Leasable(name, price, False))
            print("El equipo rentable ha sido añadido correctamente.")
            print("------------------------------------------------------")
            time.sleep(2)
            os.system("cls")
            return

        elif index == 5:
            aux.show_leasables()
            print("------------------------------------------------------")
            index = int(
                validate.validate_positive_float(input("Por favor, ingrese el número relacionado con el equipo rentable"
                                                       "a eliminar: ")))
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            try:
                aux = aux.leasables[index - 1]
            except IndexError:
                print("------------------------------------------------------")
                print("            No se ha encontrado el equipo rentable")
                print("                           solicitado.")
                print("------------------------------------------------------")
                time.sleep(2)
                os.system("cls")
                return
            else:
                aux.remove_product(index - 1)
                print("El equipo rentable ha sido eliminado satisfactoriamente.")
                time.sleep(2)
                os.system("cls")
                return

        elif index == 6:
            print("------------------------------------------------------")
            aux.modify_leseable_price()
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")

        elif index == 7:
            print("------------------------------------------------------")
            print("                  Regresando al menú")
            print("                       Principal")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            return
        else:
            print("------------------------------------------------------")
            print("                  La opción seleccionada no")
            print("                   se encuentra registrada.")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            print("------------------------------------------------------")
            print("                  Regresando al menú")
            print("                       Principal")
            print("------------------------------------------------------")
            time.sleep(2)
            os.system("cls")


def recharge_person(persons: list):
    bandera = 0
    id = 0
    aux = 0
    print("------------------- Recarga de usuarios -------------------")
    id = (validate.validate_positive_float(input("Por favor, ingrese el documento de identidad del usuario ")))
    for person in persons:
        if person.id == id:
            aux = person
            break
    os.system("cls")

    while True:
        print("------------------- Recarga de usuarios -------------------")
        print("                       Recargando a: ")
        print(f"              {aux.first_name} {aux.last_name}")
        id = validate.validate_positive_float(input("Por favor, ingrese el saldo a recargar: "))
        if input(f"¿Confirma que el saldo a recargar es de {id}? Y/N" == "Y"):
            break
        else:
            print("Reintentando. . .")
            time.sleep(1)
            os.system("cls")
    print("-----------------------------------------------------------")
    aux.money += id
    time.sleep(1)
    print("------------------- Recarga de usuarios -------------------")
    print(" \n                    ¡Recarga exitosa! \n")
    print("-----------------------------------------------------------")
    time.sleep(1)
    os.system("cls")


def indicators(persons: list, shops: list):
    cont_1 = 0
    cont_2 = 0
    cont_3 = 0
    for person in persons:
        cont_1 += person.money
        cont_2 += len(person.actual_doubts)
        for doubt in person.actual_doubts:
            cont_3 += doubt.amount
    print("---------------------- INDICADORES ----------------------")
    print("                         USUARIOS ")
    print(f"Usuarios activos: {len(persons)}")
    print(f"Monto total almacenado en los usuarios: {cont_1}")
    print(f"Monto promedio del usuario: {cont_1/len(persons)}")
    print(f"Total de deudas activas: {cont_2}")
    print(f"Cantidad promedio de deudas por usuario: {cont_2/len(persons)}")
    print(f"Deuda total de los usuarios: {cont_3}")
    print(f"Deuda promedio del usuario: {cont_3/len(persons)}\n")
    print("                         TIENDAS")
    for shop in shops:
        cont_1 += shop.money
        cont_2 += len(shop.leasables)
        cont_3 += len(shop.products)
    print(f"Tiendas activas: {len(shops)}")
    print(f"Monto total en tiendas: {cont_1}")
    print(f"Monto promedio en tiendas: {cont_1/len(shops)}")
    print(f"Total de productos rentables ofrecidos: {cont_2}")
    print(f"Promedio de productos rentables ofrecidos por tienda: {cont_2/len(shops)}")
    print(f"Total de productos ofrecidos: {cont_3}")
    print(f"Promedio de productos ofrecidos por tienda: {cont_3/len(shops)}")
    print("---------------------------------------------------------")
    input("Pressione ENTER para continuar")
    time.sleep(1)
    os.system("cls")

