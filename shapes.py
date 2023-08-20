
# https://mypy.readthedocs.io/en/stable/class_basics.html

from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y

    @abstractmethod
    def render(self) -> str:
        pass


class Circle(Shape):
    pass

    def render(self):
        return f'Circle as x:{self.x}, y:{self.y}'

c = Circle(1,2)


