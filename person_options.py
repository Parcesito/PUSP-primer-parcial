from person import Person
from bill import Bill
import validate
from shop import Shop
import time
import os
from debt import Debt
from datetime import datetime, date
from product import Product


def actualizate_debts(user: Person):
    count = 0
    for doubt in user.actual_doubts:
        count += doubt.payment_amount
    user.total_debt = count


def show_shops(shops: list[Shop]):
    print("--------------- Establecimientos disponibles ---------------")
    cont = 1
    for shop in shops:
        print(f"{cont}. {shop.name}")
        cont += 1
    print("------------------------------------------------------------")
    return


def pay_bill(user: Person, bill: Bill):
    if user.money < bill.payment_amount:
        print("------------------------------------------------------")
        print("           No ha sido posible realizar el pago")
        print("                   Saldo insuficiente.")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return False
    else:
        user.money -= bill.payment_amount
        user.history.append(bill)
        print("------------------------------------------------------\n")
        print("                    Pago realizado \n")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return True


def debt_bill(user: Person, bill: Bill):
    actualizate_debts(user)
    if user.max_doubt < bill.payment_amount + user.total_debt:
        print("------------------------------------------------------")
        print("               No ha sido almacenar la deuda ")
        print("                 Excedería su deuda máxima ")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return False
    else:
        user.actual_doubts.append(bill)
        actualizate_debts(user)
        print("------------------------------------------------------\n")
        print("                    Deuda almacenada \n")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
        return True


def purchease(user: Person, shops: list):
    index = 0
    index_2 = 0
    aux = 0
    bill = 0
    temporal_car = []
    bandera = 0
    while bandera == 0:
        show_shops(shops)
        index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado a la tienda "
                                                           "en la que desea realizar su compra: ")))
        try:
            aux = shops[index - 1]
        except IndexError:
            print("------------------------------------------------------")
            print("       No se ha encontrado el establecimiento")
            print("                       solicitado.")
            print("------------------------------------------------------")
            time.sleep(1)
            print("------------------------------------------------------\n")
            print("                  Inténtelo nuevamente \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            continue
        else:
            while True:
                aux.showproducts()
                index_2 = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado "
                                                                     "al producto que desea comprar: ")))

                try:
                    temporal_car.append(aux.products[index_2 - 1])
                except IndexError:
                    print("------------------------------------------------------")
                    print("            No se ha encontrado el producto")
                    print("                       solicitado.")
                    print("------------------------------------------------------")
                    time.sleep(1)
                    print("------------------------------------------------------\n")
                    print("                  Inténtelo nuevamente \n")
                    print("------------------------------------------------------")
                    time.sleep(1)
                    os.system("cls")
                    continue
                else:
                    print("------------------------------------------------------\n")
                    print("                    Producto añadido \n")
                    print("------------------------------------------------------")
                    time.sleep(0.5)
                    os.system("cls")
                    break
            bandera = input("¿Desea comprar otro producto? Y/N")
            if bandera == ("N" or "n"):
                bandera = 1
            else:
                bandera = 0
    index = 0
    for product in temporal_car:
        index += product.price

    bill = Bill(user, temporal_car, date.today(), "Múltiples dependencias", index)
    bill.print_bill()

    while True:
        print("-------------------- Opciones de pago --------------------")
        print("1. Pagar factura ")
        print("2. Deber factura ")
        print("3. Cancelar compra ")
        print("----------------------------------------------------------")
        option = validate.validate_positive_float(input("Por favor, ingrese el número relacionado a su método de pago"))
        if option == 1:
            if pay_bill(user, bill):
                return
        elif option == 2:
            if debt_bill(user, bill):
                return
        elif option == 3:
            print("------------------------------------------------------\n")
            print("                    Compra cancelada \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            return


def order(user: Person, shops: list[Shop]):
    index = 0
    index_2 = 0
    aux = 0
    bill = 0
    temporal_car = []
    bandera = 0

    while True:
        show_shops(shops)
        index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado a la tienda "
                                                           "en la que desea realizar su compra: ")))
        try:
            aux = shops[index - 1]
        except IndexError:
            print("------------------------------------------------------")
            print("       No se ha encontrado el establecimiento")
            print("                       solicitado.")
            print("------------------------------------------------------")
            time.sleep(1)
            print("------------------------------------------------------\n")
            print("                  Inténtelo nuevamente \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            continue
        else:
            aux.show_leasables()
            index_2 = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado al "
                                                                 "producto que desea solicitar: ")))
        try:
            temporal = aux.leasable[index_2 - 1]
        except IndexError:
            print("------------------------------------------------------")
            print("            No se ha encontrado el producto")
            print("                       solicitado.")
            print("------------------------------------------------------")
            time.sleep(1)
            print("------------------------------------------------------\n")
            print("                  Inténtelo nuevamente \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            continue
        else:
            user.actual_debts.append(Debt(aux, user, temporal.price, date.today()))
            print("------------------------------------------------------\n")
            print("                  Producto solicitado \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            break


def return_debt(user: Person):
    user.print_actual_debts()
    index = validate.validate_positive_float(input("Ingrese el número asociado al equipo retornado: "))
    try:
        aux = user.actual_debts[index - 1]
    except IndexError:
        print("------------------------------------------------------")
        print("            No se ha encontrado el producto")
        print("                       solicitado.")
        print("------------------------------------------------------")
        time.sleep(1)
        print("------------------------------------------------------\n")
        print("                  Inténtelo nuevamente \n")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
    else:
        user.actual_doubts.append(Bill(user, [Product(f"Préstamo realizado en {aux.name}", aux.price)],
                                       date.today(), aux.creditor.name, aux.amount * (date.today() - aux.date)))
        user.actual_debts.pop(index - 1)
        print("------------------------------------------------------\n")
        print("             Producto retornado de forma efectiva \n")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")


def pay_archive_bill(user):
    print("--------------------------- Deudas actuales ----------------------")
    for debt in user.actual_doubts:
        print(f"{debt.name} \t\t {debt.payment_amount}")
    print("------------------------------------------------------------------")
    index = validate.validate_positive_float(input("Por favor, ingrese el número relacionado a "
                                                   "la deuda que desea pagar"))
    try:
        aux = user.actual_doubts[index - 1]
    except IndexError:
        print("------------------------------------------------------\n")
        print("                    Deuda no encontrada \n")
        print("------------------------------------------------------")
        time.sleep(1)
        os.system("cls")
    else:
        pay_bill(user, aux)


def user_menu(user: Person, shops: list):
    while True:
        print(f"Usuario: {user.name} {user.last_name}")
        print("------------------ Menú de usuario ------------------")
        print("1. Revisar saldo y deudas actuales")
        print("2. Revisar préstamos activos")
        print("3. Realizar compra")
        print("4. Apartar equipo")
        print("5. Pagar deudas")
        print("6. Devolver equipos")
        print("7. Cerrar sesión y salir")
        print("-----------------------------------------------------\n")
        option = validate.validate_positive_float(input("Por favor, ingrese el número relacionado con la acción"
                                                        "que desea ejecutar"))
        os.system("cls")
        if option == 1:
            actualizate_debts(user)
            print("------------------ Saldos actuales ------------------")
            print(f"El presupuesto actual es de: {user.money}")
            print(f"La deuda actual es de {user.total_debt}")
            print("-----------------------------------------------------")
            input("Por favor, ingrese ENTER para volver al menú principal")
            os.system("cls")

        elif option == 2:
            user.print_actual_debts()
            input("Por favor, ingrese ENTER para volver al menú principal")
            os.system("cls")

        elif option == 3:
            purchease(user, shops)

        elif option == 4:
            order(user, shops)

        elif option == 5:
            pay_archive_bill(user)
        elif option == 6:
            return_debt(user)
        elif option == 7:
            print("------------------------------------------------------\n")
            print("                    Cerrando sesión\n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            print("------------------------------------------------------\n")
            print("                    Sesión finalizada \n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
            break

        else:
            print("------------------------------------------------------\n")
            print("                    Opción no reconocida")
            print("                    Inténtelo nuevamente\n")
            print("------------------------------------------------------")
            time.sleep(1)
            os.system("cls")
