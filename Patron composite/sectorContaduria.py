from component import Isueldo

class SectorCont(Isueldo):
    
    def __init__(self, sueldo):
        self._sueldo = sueldo

    def get_sueldo(self):
        print(f"Sector contaduria:{self._sueldo}")