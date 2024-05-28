# -*- coding: utf-8 -*-
class InvalidDataException(Exception):
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return (f'Недопустимое значение: {self.age}\n'
                f'Возраст должен быть в диапазоне от {self.minage} до {self.maxage}')


class ProcessingException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Недопустимое значение {self.name} здесь должно быть имя'

class Person:

    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 100
        if minage < age < maxage:
            self.__age = age
        else:
            raise InvalidDataException(age, minage, maxage)
        if name == str(name):
            self.__name
        else:
            raise ProcessingException(name)


    def d_inf(self):
        print(f'Имя: {self.__name} возраст {self.__age}')

try:
    artur = Person('Artur', 40)


    denis = Person(45, 31)


    masha = Person('Маша', 0.5)
    artur.d_inf()
    denis.d_inf()
    masha.d_inf()

except InvalidDataException as e:
    print(e)
except ProcessingException as ex:
    print(ex)

