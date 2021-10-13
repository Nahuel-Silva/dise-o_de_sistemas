#Abstract Factory
from abc import ABC, abstractmethod

class Fabrica():
    @abstractmethod
    def crear_coche(self):
        pass

    @abstractmethod
    def crear_motor(self):
        pass

    @abstractmethod
    def crear_chasis(self):
        pass
