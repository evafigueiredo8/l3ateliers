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
    print("1ère ligne :", colonne)
    print(matrice[1])
    for i in range(len(matrice)):
        colonne = []
        colonne.append(matrice[i,2])
        print("3ème colonne :", colonne)
    matrice2x2 = np.array(([0]*2,[0]*2))
    for i in range(len(matrice2x2)):
        for e in range(len(matrice2x2[i])):
            matrice2x2[i,e] = matrice[i,e]
    print(matrice2x2)


slicing_indexation_matrcice(ajout_matrice(matrice3x3()))