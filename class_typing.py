from typing import Protocol

class Shape(Protocol):
    def area(self) -> float:... # Ellipsis prevents warning that the method does not return


class Circle:
    def area(self) -> float:
        return 0.1

c: Shape = Circle()


