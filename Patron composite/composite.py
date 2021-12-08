from component import Isueldo

class SectorGeneral(Isueldo):
    
    def __init__(self,sueldo):
        self._sueldo = sueldo
        self._sueldoG = sueldo
        self._sectoresT = []

    def add(self, sectores):
        self._sectoresT.append(sectores)
        self._sueldo += sectores._sueldo

    def get_sueldo(self):
        print(f"Sueldo del sector general: {self._sueldoG}")
        for sector in self._sectoresT:
            sector.get_sueldo()
        print(f"Cantidad total de los sueldos de todos los sectores: {self._sueldo}")

