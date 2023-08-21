from typing import Protocol

class Connectable(Protocol):
    def call(self) -> None: ...
    def text(self) -> None: ...

class Touchable(Protocol):
    def slide_to_unlock(self) -> None: ...

class Galaxy:
    def call(self) -> None:
        print('call with Galaxy.')
    def text(self) -> None: ...
        print('text with Galaxy.')
    def slide_to_unlock(self) -> None:
        print('slide to unlock Galaxy.')


class Nokia:
    def call(self) -> None:
        print('call with Galaxy.')
    def text(self) -> None: ...
        print('text with Galaxy.')
    def slide_to_unlock(self) -> None:
        return NotImplementedError('Not implemented')


connectable_devices: list[Connectable] = [Galaxy()]
touchable_devices: list[Touchable] = [Galaxy(), Nokia()]

