from abc import ABCMeta, abstractmethod

class Ifactory(metaclass=ABCMeta):

    @abstractmethod
    def creador_de_triangulos(self, ladoA, ladoB, ladoC):
        pass