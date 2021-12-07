from triangulo import *

class Equilatero(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)
    
    def get_description(self):
        print("Triangulo Equilatero")

    def get_superficie(self):
        print("Superficie Equilatero")