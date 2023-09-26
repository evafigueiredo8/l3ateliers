import numpy as np
import random

def matriceAdjacence(S : list, A : list) -> object :
    longueur = len(S)
    adjacence = np.zeros((longueur,longueur))
    for i in A:
        adjacence[i[0],i[1]] = 1
    return adjacence

print(matriceAdjacence(([0,1,2]),[(1,2),(2,0),(0,0)]))

def matriceAdjacencePond(S : list, A : list) -> object :
    longueur = len(S)
    adjacence = np.zeros((longueur,longueur))
    for i in A:
        adjacence[i[0],i[1]] = i[2]
    return adjacence

print(matriceAdjacencePond(([0,1,2]),[(1,2,3),(2,0,9),(0,0,2)]))

def lireMatriceFichier(nomfichier) -> object : # pas fini
    matricefichier = np.array([])
    contenu = nomfichier.read()
    print(contenu)
    nomfichier.close()
    while i != ' ':
        for i in contenu:
            matricefichier += 1
    matricefichier = np.array([])
    return matricefichier

fichier = open('graph0.txt', 'r')
print(lireMatriceFichier(fichier))