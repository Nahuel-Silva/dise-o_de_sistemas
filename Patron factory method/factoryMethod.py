from equilatero import Equilatero
from escaleno import Escaleno
from ifactory import *
from isosceles import Isosceles

class FactoryMethod(Ifactory):

    def creador_de_triangulos(self, ladoA, ladoB, ladoC):
        if ladoA == ladoB and ladoB == ladoC:
            return Equilatero(ladoA, ladoB, ladoC)
        elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
            return Escaleno(ladoA, ladoB, ladoC)
        else:
            return Isosceles(ladoA, ladoC, ladoB)
