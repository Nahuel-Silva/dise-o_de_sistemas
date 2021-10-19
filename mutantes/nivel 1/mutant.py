from probar_random import *
import numpy as np
from diagonales import *
from filas_columnas import *

def mutant(dna):
    matriz = np.array(dna)
    contador_diag = diagonales(matriz)
    contador_colfil = colAndfil(matriz)
    if (contador_diag+contador_colfil) >= 2:
        print("Mutante!")
        # print(contador_diag+contador_colfil)
    else:
        print("Humano!")
        # print(contador_diag+contador_colfil)
    


