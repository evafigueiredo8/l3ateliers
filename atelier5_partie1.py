#Question 1

def somme(lst:list) -> int:
    if lst == []:
        return 0
    else:
        return lst[0]*somme(lst[1:]) #lst[1:] renvoie tous les elements de la liste sauf le 1er

#Question 2

def factorielle_recursive(nombre:int) -> int:
    if nombre == 0:
        return 1
    else:
        return nombre*factorielle_recursive(nombre-1)

nombre = 3
resultat = factorielle_recursive(nombre)
print("Le factoriel de", nombre, "est :", resultat)

#Exercice au tableau

#Ex1
def longueur(lst:list) -> int: #renvoie le nb d'elts de la liste
    if lst == []:
        return 0
    else:
        return 1+longueur(lst[1:])

lst = []
resultat = longueur(lst)
print("La liste contient ", resultat, "éléments.")

#Ex2
def findMin(lst:list) -> int: #trouve le minimum d'une liste et le retourne
    if lst == []:
        return None
    if len(lst) == 1:
        return lst[0]
    if lst[0] < findMin(lst[1:]):
        return lst[0]
    else:
        return findMin(lst[1:])

lst = [2,5,7,1,3]
resultat = findMin(lst)
print("Le minimum de la liste est", resultat, ".")

#Ex3
def ListPairs(lst:list) -> list: #retourne une liste des éléments pairs de lst
    if lst == []:
        return []
    if lst[0]%2 == 0:
        return [lst[0]] + ListPairs(lst[1:])
    else:
        return ListPairs(lst[1:])

lst = [2,5,7,1,3]
resultat = ListPairs(lst)
print("La liste des pairs est : ", resultat)

#Ex4
def ConcatList(lst: list) -> list: #concatène les listes contenues dans la liste lst et retourne une liste plate constituée des elts simples
    if lst == []:
        return []
    else:
        return lst[0] + ConcatList(lst[1:])

lst=[[0,1],[2,3],[4],[6,7]]
resultat = ConcatList(lst)
print("La liste plate est :", resultat)
