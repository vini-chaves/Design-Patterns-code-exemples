from .interfaces import Observer, Subject
from typing import Type

class ConcreteObserverA(Observer):
    def __init__(self):
        super().__init__()

    def update(self, subject: Type[Subject]) -> None:
        if subject._state < 4:
            print("ConcreteObserverA: Reacted to the event")

class ConcreteObserverB(Observer):
    def __init__(self):
        super().__init__()

    def update(self, subject: Type[Subject]) -> None:
        if subject._state == 0 or subject._state >= 4:
            print("ConcreteObserverB: Reacted to the event")