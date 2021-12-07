#ProductA
from abc import ABCMeta, abstractmethod

class Motor(metaclass=ABCMeta):
    @abstractmethod
    def funcion_motor(self):
        pass