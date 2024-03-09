from person import Person
from bill import Bill
import validate
from shop import Shop
import time
import os
from datetime import datetime


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
        else:
            aux.showproducts()
            index_2 = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado al producto "
                                                                 "que desea comprar: ")))
            while True:
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

    bill = Bill(user, temporal_car, datetime.date, "Múltiples dependencias", index)
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

def order(user: Person, shops: list):
