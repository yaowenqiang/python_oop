import math
class A:
    def instance_methods(self):
        pass

    @classmethod
    def class_methods(cls):
        pass

    @staticmethod
    def static_methods():
        pass

class Address:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def from_url(cls, url):
        print(cls)
        ip, port = url.split(':')
        return cls(ip, port)


a1 = Address('127.0.0.1', 8000)
print(a1.ip, a1.port)
a2 = Address.from_url('127.0.0.1:9000')
print(a2.ip, a2.port)


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def render(self):
        return f'Circle with radius {self.radius}'

    @staticmethod
    def radians_to_degrees(radians):
        return math.degrees(radians)

print(Circle.radians_to_degrees(math.pi))
print(Circle.radians_to_degrees(2 * math.pi))
