from abc import ABCMeta, abstractstaticmethod

class Ifactory(metaclass=ABCMeta):

    @abstractstaticmethod
    def creador_de_triangulos(self, ladoA, ladoB, ladoC):
        pass