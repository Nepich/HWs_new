import copy
from abc import ABC, abstractmethod
import keyboard


class Player(ABC):
    @abstractmethod
    def observe(self, observer: Observer):
        pass

    @abstractmethod
    def stop_observe(self, observer: Observer):
        pass

    @abstractmethod
    def tell(self, key):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Player, coord):
        pass


class ConcretePlayer(Player):

    _observer: Observer = None
    __coord = [10, 10]

    def observe(self, observer: Observer):
        self._observer = observer

    def stop_observe(self, observer: Observer):
        self._observer = None

    def tell(self, key):
        self._observer.update(self, key)

    def walk(self, key):
        changed = copy.copy(self.__coord)
        if key == 'w':
            self.__coord[0] += 1
        elif key == 's':
            self.__coord[0] -= 1
        elif key == 'a':
            self.__coord[1] -= 1
        elif key == 'd':
            self.__coord[1] += 1
        changed = [changed[0] - self.__coord[0], changed[0] - self.__coord[0]]
        self.tell(changed)


class ConcreteObserver(Observer):

    __coord = [5, 5]

    def update(self, subject: Player, coord):
        self.__coord = [self.__coord[0] - coord[0], self.__coord[1] - coord[1]]



