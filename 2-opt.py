import numpy as np
import generate_matrix
from itertools import combinations 
import random
import matplotlib.pyplot as plt

def update_custo(d, n1, n2, n3, n4):
    return d[n1][n3] + d[n2][n4] - d[n1][n2] - d[n3][n4]

def h_2opt(rota, d):
    rota_melhor = rota
    flag = True
    while flag:
        flag = False
        for i in range(1, len(rota) - 2):
            for j in range(i + 1, len(rota)):
                if j - i == 1: continue
                if update_custo(d, rota_melhor[i - 1], rota_melhor[i], rota_melhor[j - 1], rota_melhor[j]) < 0:
                    rota_melhor[i:j] = rota_melhor[j - 1:i - 1:-1]
                    flag = True
        rota = rota_melhor
    return rota_melhor

def print_resultado(rota, coordenadas):
    d_plot = np.concatenate((np.array([coordenadas[rota[i]] for i in range(len(rota))]),np.array([coordenadas[rota[0]]])))

    plt.scatter(coordenadas[:,0],coordenadas[:,1])

    plt.plot(d_plot[:,0],d_plot[:,1])
    
    for i, txt in enumerate(rota):
        plt.annotate(str(rota[i]), coordenadas[rota[i]])

    plt.show()

def calcula_custo(d, rota):
    dT = 0
    for i in range(0,len(rota)):
        dT +=  d[rota[i]][rota[i-1]]
    dT += d[rota[i]][rota[0]]

    return dT

if __name__ == '__main__':
    print("ENIGMA DAS GALÁXIAS\n")

    d, galaxias, coordenadas = generate_matrix.generate_matrix('wi29.tsp')
    G = len(d)
    d = np.array(d)
    coordenadas = np.array(coordenadas)
    np.fill_diagonal(d, 0)
    print(d)
    print(G)

    rota_inicial = list(range(G))
    random.shuffle(rota_inicial)
    print(rota_inicial)

    rota_top = h_2opt(rota_inicial, d)
    print(rota_top)
    print(calcula_custo(d, rota_top))

    print_resultado(rota_top, coordenadas)