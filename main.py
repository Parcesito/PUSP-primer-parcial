import admin_options
import person_options
import time
import os
from person import Person
from product import Product
from shop import Shop
from user import User
from datetime import date
from leasable import Leasable


def pusp(users: list, admins: list,  shops: list[Shop]):
    bandera = 0
    while True:
        print("--------------------- Inicio de sesión ---------------------\n")
        name = input("                Usuario: ")
        password = input("                contraseña:")
        print("\n--------------------------------------------------------------")

        for user in users:
            if user.user == name and user.password == password:
                bandera = 1
                person_options.user_menu(user, shops)
                break
        if bandera == 0:
            for admin in admins:
                if admin.user == name and admin.password == password:
                    bandera = 1
                    admin_options.admin_menu(users, shops)
                    break

        if bandera == 0:
            print("--------------------------------------------------------------\n")
            print("                     Usuario no encontrado \n")
            print("--------------------------------------------------------------\n")

        print("--------------------- Inicio de sesión ---------------------\n")
        bandera = input("¿Desea iniciar sesión nuevamente Y/N: ")
        if bandera == "Y":
            continue
        print("--------------------------------------------------------------\n")
        print("            ¡Muchas gracias por utilizar el programa! \n")
        print("--------------------------------------------------------------\n")
        break


users = [Person(2000, "Carlos", "Álveres", date(1980, 12, 5), "user123",
               "12345", False, 15000)]

admins = [User(1000, "Jhon", "Doe", date(1980, 12, 28), "admin123",
       "12345", True)]
shops = [Shop("Gimnasio")]
shops[0].add_leasable(Leasable("Bicicleta", 4000, False))
shops[0].add_product(Product("Bebida energética", 5000))
pusp(users, admins, shops)
