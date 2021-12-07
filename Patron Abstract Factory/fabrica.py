#Abstract Factory
from abc import ABCMeta, abstractmethod

class Fabrica(metaclass=ABCMeta):
    @abstractmethod
    def crear_coche(self):
        pass

    @abstractmethod
    def crear_motor(self):
        pass

    @abstractmethod
    def crear_chasis(self):
        pass
