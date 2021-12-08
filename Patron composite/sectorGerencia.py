from component import Isueldo

class SectorGerencia(Isueldo):
    
    def __init__(self, sueldo):
        self._sueldo = sueldo

    def get_sueldo(self):
        print(f"Sector gerencial:{self._sueldo}")