import user
import bill
import debt
import validate
from datetime import date


class Person(user.User):
    def __init__(self, id: int, name: str, last_name: str, birth_date: date, user: str, password: str, admin: bool,
                 max_doubt: float, ):
        super().__init__(id, name, last_name, birth_date, user, password, admin)
        self.__max_doubt = max_doubt
        self.__money = 0
        self.__history = []
        self.__actual_doubts = []

    @property
    def max_doubt(self):
        return self.__max_doubt

    @property
    def money(self):
        return self.__money

    @property
    def history(self):
        return self.__history

    @property
    def actual_doubts(self):
        return self.__actual_doubts

    @max_doubt.setter
    def max_doubt(self, max_doubt: float):
        self.__max_doubt = max_doubt

    @money.setter
    def money(self, money: float):
        self.__money = money

    def add_purchease(self, new: bill):
        self.__history.append(new)

    def add_debt(self, new: debt):
        self.__actual_doubts.append(new)

    def exceeded_limit(self):  # Función para saber si se ha superado el límite de deuda
        amount = 0
        for debt in self.__actual_doubts:
            amount += debt.amount

        if amount > self.__max_doubt:
            return True
        else:
            return False

    def pay_debt(self):
        cont = 1
        index = 0
        print("------ Lista de deudas existentes --------")
        for debt in self.__actual_doubts:
            print(f"{cont}. {debt.creditor} . . . . .  {debt.amount}")
            cont += 1

        index = int(validate.validate_positive_float(input("Por favor, ingrese el número relacionado a la deuda que "
                                                           "desea pagar: ")))

        try:
            cont = self.__actual_doubts[index-1].amount
        except IndexError:
            print("No ha sido posible realizar el pago de la deuda")
            return
        else:
            if cont > self.money:
                print("No posee el monto necesario para saldar esta deuda")
                return

            else:
                self.__money -= cont
                self.__actual_doubts[index-1].creditor.money += cont
                self.__actual_doubts.pop(index-1)
                print("La deuda se ha saldado exitosamente. Su nuevo monto es de ", self.__money)
