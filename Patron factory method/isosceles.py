from triangulo import *

class Isosceles(Triangulo):
    def __init__(self, ladoA, ladoB, ladoC):
        super().__init__(ladoA, ladoB, ladoC)
    
    def get_description(self):
        print("Triangulo Isosceles")

    def get_superficie(self):
        print("Superficie Isosceles")