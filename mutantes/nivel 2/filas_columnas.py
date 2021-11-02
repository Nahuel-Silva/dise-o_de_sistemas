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