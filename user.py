from datetime import date


class User(object):
    def __init__(self, id: int, name: str, last_name: str, birth_date: date, user: str, password: str, admin: bool):
        self.__id = id
        self.__name = name
        self.__last_name = last_name
        self.__birth_date = birth_date
        self.__user = user
        self.__password = password
        self.__admin = admin
        # Se declaran todos los atributos ocultos para evitar que sean modificados de forma inadecuada.

    # Funciones para acceder a los atributos.

    @property
    def id(self):
        return self.__id

    @property
    def admin(self):
        return self

    @property
    def name(self):
        return self.__name

    @property
    def last_name(self):
        return self.__last_name


    @property
    def birth_date(self):
        return self.__birth_date

    @property
    def user(self):
        return self.__user

    @property
    def password(self):
        return self.__password

    # Funciones para modificar los atributos.
    # No existe una función para modificar el atributo "Admin" pues este se espera inmutable para cada usuario
    @password.setter
    def password(self, password: str):
        self.__password = password

    @user.setter
    def user(self, user: str):
        self.__user = user

    @birth_date.setter
    def birth_date(self, birth_date: date):
        self.__birth_date = birth_date

    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @id.setter
    def id(self, id: int):
        self.__id = id
