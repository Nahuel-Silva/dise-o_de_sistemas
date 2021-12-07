from triangulo import *

class Escaleno(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)
    
    def get_description(self):
        print("Triangulo Escaleno")

    def get_superficie(self):
        print("Superficie Escaleno")