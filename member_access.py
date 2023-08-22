from pprint import pprint
class Employee:
    def __init__(self, name ,salary):
        self._name = name
        self._salary = salary

        # name mangling

        self.__name = name
        self.__salary = salary

    def get_info(self):
        return f'{self._name}, ${self._salary}'

    def get_info2(self):
        return f'{self.__name}, ${self.__salary}'


e = Employee('Vera', 2000)
e._salary = 3000
e.__salary = 4000
pprint(e.get_info())
pprint(e.get_info2())
e._Employee__salary = 500
pprint(e.get_info2())
# pprint(dir(e))
