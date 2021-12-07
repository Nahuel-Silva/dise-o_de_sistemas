#ProductB
from abc import ABCMeta, abstractmethod

class Coche(metaclass=ABCMeta):
    
    @abstractmethod
    def funcion_coche(self):
        pass