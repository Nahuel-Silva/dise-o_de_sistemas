import numpy as np

a = ["A","A","A","A"]
t = ["T","T","T","T"]
g = ["G","G","G","G"]
c = ["C","C","C","C"]

def colAndfil(matriz):

    #Trabajamos con las filas
    lista1 = []
    for i in matriz:
        for j in range(len(i)+1):
            if len(i[:j]) == 4:
                lista1.append(list(i[:j]))
            if len(i[j:]) == 4:
                lista1.append(list(i[j:]))
            if len(i[:j]) == 5:
                corte = len(i[:j]) - 4
                lista1.append(list(i[corte:j]))
    con_colfil = 0
    for i in range(len(lista1)):
        if a == lista1[i]:
            con_colfil += 1
        elif t == lista1[i]:
            con_colfil += 1
        elif g == lista1[i]:
            con_colfil += 1
        elif c == lista1[i]:
            con_colfil += 1
    
    #Trabajamos con las columnas
    transpuesta = np.transpose(matriz)
    lista2 = []
    for i in transpuesta:
        for j in range(len(i)+1):
            if len(i[:j]) == 4:
                lista2.append(list(i[:j]))
            if len(i[j:]) == 4:
                lista2.append(list(i[j:]))
            if len(i[:j]) == 5:
                corte = len(i[:j]) - 4
                lista2.append(list(i[corte:j]))

    for i in range(len(lista2)):
        if a == lista2[i]:
            con_colfil += 1
        elif t == lista2[i]:
            con_colfil += 1
        elif g == lista2[i]:
            con_colfil += 1
        elif c == lista2[i]:
            con_colfil += 1

    return con_colfil

def diagonales(matriz):

    #Trabajamos con la matriz principal
    central = np.diag(matriz)
    lista1 = []
    for i in range(len(central)+1):
        if len(central[i:]) == 4:
            lista1.append(list(central[i:]))
        if len(central[:i]) == 4:
            lista1.append(list(central[:i]))
        if len(central[:i]) == 5:
            corte = len(central[:i]) - 4
            lista1.append(list(central[corte:i]))
    
    contador_ppal = 0
    for i in range(len(lista1)):
        if a == lista1[i]:
            contador_ppal += 1
        elif t == lista1[i]:
            contador_ppal += 1
        elif g == lista1[i]:
            contador_ppal += 1
        elif c == lista1[i]:
            contador_ppal += 1
    
    #Trabajamos con las diagonales sobre la diagonal principal
    lista2 = []
    diag_sup= []
    rango = len(central) - 3
    for i in range(1,rango):
        superiores = np.diag(matriz, i)
        diag_sup.append(list(superiores))
    for i in diag_sup:
        if len(i) != 4:
            for j in range(len(i)+1):
                if len(i[j:]) == 4:
                    lista2.append(list(i[j:]))
                if len(i[:j]) == 4:
                    lista2.append(list(i[:j]))
        else:
            lista2.append(list(i))
            
    for i in range(len(lista2)):
        if a == lista2[i]:
            contador_ppal += 1
        elif t == lista2[i]:
            contador_ppal += 1
        elif g == lista2[i]:
            contador_ppal += 1
        elif c == lista2[i]:
            contador_ppal += 1
    
    #Trabajamos con las diagonales dejabo de la diagonal principal
    lista3 = []
    diag_inf= []
    rango = len(central) - 3
    for i in range(1,rango):
        inferiores = np.diag(matriz, -i)
        diag_sup.append(list(inferiores))
    for i in diag_inf:
        if len(i) != 4:
            for j in range(len(i)+1):
                if len(i[j:]) == 4:
                    lista3.append(list(i[j:]))
                if len(i[:j]) == 4:
                    lista3.append(list(i[:j]))
        else:
            lista3.append(list(i))
            
    # contador_inf = 0
    for i in range(len(lista3)):
        if a == lista3[i]:
            contador_ppal += 1
        elif t == lista3[i]:
            contador_ppal += 1
        elif g == lista3[i]:
            contador_ppal += 1
        elif c == lista3[i]:
            contador_ppal += 1

    return contador_ppal

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
    


