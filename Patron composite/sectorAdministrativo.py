from composite import *

class SectorAdmin(Isueldo):
    
    def __init__(self, sueldo):
        self._sueldo = sueldo

    def get_sueldo(self):
        print(f"Sector administrativo:{self._sueldo}")