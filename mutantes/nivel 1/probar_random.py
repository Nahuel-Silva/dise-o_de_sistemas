import random
import numpy as np

def random_dna():
    adn = ['A','T','C','G']
    dna = []
    for _ in range(6):
        lista = []
        for _ in range(6): 
            lista.append(random.choice(adn))
        dna.append(lista)
    return np.array(dna)