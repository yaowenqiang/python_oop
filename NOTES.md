Not part of this projcet

> multiple inheritance
> mixins
> singletion




> pythonforeveryone.com


static type checking

+ mypy
+ pyright

----------------    | -------------------------
type(d) is Header  | True if d is of type Header
isinstance(d, Header) | True if d is of type Header or any of its subclasses
type(d) ==  Header  | Do not us! Checks for value equality, Can be overridden in custom classes with unexpected behavior


# protocol classes

## protocol ducktyping runtime

+ __str__ String protocol
+ __len__ Length protocol
+ __iter__ 


## protocol Structural subtyping static ducktyping


class A(Protocol)




pep 544

https://peps.python.org/pep-0544/


subtype by name

class Shape:
    def area(self) -> float:...

class Circle(Shape):
    def area(self) -> float:
        return 42.0

subtype throught protocol

from typing import Protocol
class Shape(Protocol):
    def rea(self) -> float:...

class Circle:
    def area(self) -> float:
        return 42.0

    





#  Private variables

> https://docs.python.org/3/tutorial/classes.html

> It is not possible to make things private in Python!
> you can indicate things 'should' be private

