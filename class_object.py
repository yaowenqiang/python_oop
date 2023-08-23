from pprint import pprint
class Employee:
    pass

print(Employee)
print(Employee())
print(type(Employee))
print(dir())
e = Employee()
print(type(e))
print(type(e) is Employee)

class Attendent:
    job_title = 'ceo'
    def __init__(self, name):
        self.name = name
        #self.job_title = job_title

    def __str__(self):
        return f'{self.name}, {self.job_title}'


#vera = Attendent('Vera', 'cto')
#dave = Attendent('Dave', 'coo')
vera = Attendent('Vera')
dave = Attendent('Dave')
print(vera)
print(dave)

vera.job_title = 'coo'
dave.job_title = 'coo'
print(vera)
print(dave)
