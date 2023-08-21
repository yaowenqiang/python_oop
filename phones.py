from abc import ABC
from abc import abstractmethod

class Phone(ABC):
    @abstractmethod
    def call(self) -> None: ...
    @abstractmethod
    def text(self) -> None: ...
    @abstractmethod
    def slide_to_unlock(self) -> None: ...

class Galaxy(Phone):
    def call(self) -> None:
        print('call with Galaxy.')
    def text(self) -> None: ...
        print('text with Galaxy.')
    def slide_to_unlock(self) -> None:
        print('slide to unlock Galaxy.')


class Nokia(Phone):
    def call(self) -> None:
        print('call with Galaxy.')
    def text(self) -> None: ...
        print('text with Galaxy.')
    def slide_to_unlock(self) -> None:
        return NotImplementedError('Not implemented')

# fat interface

