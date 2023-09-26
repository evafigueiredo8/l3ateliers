import numpy as np
import random

#Question 1

def my_searchsorted(table : object, elt : int) -> int:
    indice = -1
    i = 0
    while elt != table[i] :
        i += 1
    if elt == table[i] :
        indice = i
    return indice

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 6)
print(x)

x = my_searchsorted(arr, 8)
print(x)

#Question 2

def my_where(table : object, elt : int )-> list:
    indices = []
    for i in range(len(table)):
        if elt == table[i] :
            indices.append(i)
    return indices

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

x = my_where(arr,4)
print(x)
print("----------------------")

#Question 3

def my_add(tableA : object, tableB : object)-> object:
    if tableA.shape == tableB.shape:
        for i in range(len(tableA)):
            for e in range(len(tableA[i])):
                tableA[i,e] += tableB[i,e] 
    return tableA

A = np.array(([3,1],[6,4]))
B = np.array(([1,8],[4,2]))
R = A + B 
print(R)

R = my_add(A,B)
print(R)

#Autres exercices autour des matrices
print("-----------")
#1
def matrice3x3() -> object:
    matrice = np.array(([0]*3,[0]*3,[0]*3))
    for i in range(len(matrice)):
        for e in range(len(matrice[i])):
            matrice[i,e] = random.randint(1,9)
    return matrice

#2
def ajout_matrice(matrice: object) -> object:
    #print(matrice)
    for i in range(len(matrice)):
        for e in range(len(matrice[i])):
            matrice[i,e] += 10
    #print(matrice)
    for i in range(len(matrice)):
        for e in range(len(matrice[i])):
            matrice[i,e] *= 2
    print(matrice)
    return matrice

#3
def slicing_indexation_matrcice(matrice: object) -> object:
    print("1ère ligne :")
    print(matrice[1])
    print("3ème colonne :")
    for i in range(len(matrice)):
        colonne = []
        colonne.append(matrice[i,2])
        print(colonne)
    matrice2x2 = np.array(([0]*2,[0]*2))
    for i in range(len(matrice2x2)):
        for e in range(len(matrice2x2[i])):
            matrice2x2[i,e] = matrice[i,e]
    print(matrice2x2)


slicing_indexation_matrcice(ajout_matrice(matrice3x3()))

#Exercice 2

matriceA = np.array(([0]*4,[0]*4,[0]*4,[0]*4))
for i in range(len(matriceA)):
    for e in range(len(matriceA[i])):
        matriceA[i,e] = random.randint(0,10)

matriceI = np.array(([1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]))

def matrice_trace(matrice : object) -> object:
    somme = 0
    colonne = 0
    while colonne < len(matrice) :
        for ligne in range(len(matrice)):
            somme += matrice[ligne,colonne]
            colonne += 1
    return somme

matrice = np.array(([2,2,7],[2,2,3],[7,3,2]))

def est_symetrique(matrice : object) -> bool:
    symetrique = True
    for ligne in range(len(matrice)):
        for colonne in range(len(matrice[i])):
            if matrice[ligne,colonne] != matrice[colonne,ligne] :
                symetrique = False
    return symetrique

def produit_diagonal(matrice : object) -> object:
    produit = 1
    colonne = 0
    while colonne < len(matrice) :
        for ligne in range(len(matrice)):
            produit *= matrice[ligne,colonne]
            colonne += 1
    return produit

#3

matriceAT = np.array(([0]*4,[0]*4,[0]*4,[0]*4))
for i in range(len(matriceA)):
    for j in range(len(matriceA)):
        matriceAT[j,i] = matriceA[i,j]
matrice = (matriceA+matriceAT)/2

print(matriceA)
print(matriceAT)
print(est_symetrique(matrice))
print(produit_diagonal(matriceI))

#4

matrice = np.linalg.inv(matriceA) 
print(np.matmul(matrice,matriceA))