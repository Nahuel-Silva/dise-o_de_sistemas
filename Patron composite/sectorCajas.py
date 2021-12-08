from component import Isueldo

class SectorCajas(Isueldo):
    
    def __init__(self, sueldo):
        self._sueldo = sueldo

    def get_sueldo(self):
        print(f"Sector cajas:{self._sueldo}")