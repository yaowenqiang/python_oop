class Employee:
    def __init__(self, name):
        self.name = name
        self._salary = None

    def get_salary(self):
        return self._salary

    def set_salary(self, value):
        if value > 5000:
            raise ValueError('Maximum salary is 5000')
        self._salary = value

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value > 5000:
            raise ValueError('Maximum salary is 5000')
        self._salary = value



e = Employee('jack')
# e._salary = 100
e.set_salary(300)
print(e.get_salary())
#e.set_salary(100000)
e.salary = 600
print(e.salary)

e.salary = 1000000
print(e.salary)
