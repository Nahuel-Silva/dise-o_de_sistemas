from composite import *
from sectorAdministrativo import *
from sectorCajas import *
from sectorContaduria import *
from sectorGerencia import *

def main():
    sectorAdmin = SectorAdmin(2500)
    sectorCajas = SectorCajas(500)
    sectorCont = SectorCont(2500)
    sectorGerencia = SectorGerencia(4000)

    composite = SectorGeneral(7000)
    composite.add(sectorAdmin)
    composite.add(sectorCajas)
    composite.add(sectorCont)
    composite.add(sectorGerencia)
    composite.get_sueldo()



if __name__=="__main__":
    main()