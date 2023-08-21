from abc import ABC
from abc import abstractmethod

class Shape(ABC):
    @abstractmethod
    def renderise(self) -> str: ...
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def points(self) -> int: ...
    @abstractmethod
    def angle(self) -> float: ...

class Star(Shap)):
    def renderise(self) -> str:
        return 'Start geometry'
    def area(self) -> float:
        return 32.0
    def points(self) -> int:
        return 9
    def angle(self) -> float:
        raise NotImplementedError

class Circle(Shap)):
    def renderise(self) -> str:
        return 'Circle geometry'
    def area(self) -> float:
        return 42.0
    def points(self) -> int:
        raise NotImplementedError
    def angle(self) -> float:
        raise NotImplementedError

class Parallelogram(Shap)):
    def renderise(self) -> str:
        return 'Parallelogram geometry'
    def area(self) -> float:
        return 38.0
    def points(self) -> int:
        raise NotImplementedError
    def angle(self) -> float:
        return 38.0
