from abc import ABCMeta, abstractmethod

class Triangulo(metaclass=ABCMeta):

    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC

    @abstractmethod
    def get_description():
        pass
    
    @abstractmethod
    def get_superficie():
        pass