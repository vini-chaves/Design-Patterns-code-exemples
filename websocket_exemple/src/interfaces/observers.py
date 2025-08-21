
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def subscribe(self, client) -> None:
        pass

    @abstractmethod
    def unsubscribe(self, client) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass

