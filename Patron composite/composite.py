from isueldo import *

class Composite(Isueldo):
    
    def __init__(self,sueldo):
        self._sueldo = sueldo
        self._sectoresT = []

    def add(self, sectores):
        self._sectoresT.append(sectores)
        self._sueldo += sectores._sueldo

    def get_sueldo(self):
        sueldo_total = 0
        for i in self._sectoresT:
            i.get_sueldo()
        print(f"Cantidad total de los sueldos de todos los sectores: {self._sueldo}")

