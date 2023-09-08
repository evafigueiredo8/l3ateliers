import math

def position1(lst = list, elt = int) -> int :
    """Permet avec une boucle for range de trouver la position d'une valeur elt dans la liste lst

    Args:
        lst (_type_, optional): _description_. Defaults to list.
        elt (_type_, optional): _description_. Defaults to int.

    Returns:
        int: _description_
    """
    indice = -1
    for i in range (len(lst)) :
        if elt == lst[i] :
            indice = i
    return indice

print(position1([2,5,3,4,6,9],4))

def position2(lst = list, elt = int) -> int :
    """Permet avec une boucle for range de trouver la position d'une valeur elt dans la liste lst

    Args:
        lst (_type_, optional): _description_. Defaults to list.
        elt (_type_, optional): _description_. Defaults to int.

    Returns:
        int: _description_
    """
    indice = -1
    i = 0
    while elt != lst[i] :
        i += 1
    if elt == lst[i] :
        indice = i
    return indice

print(position2([2,5,3,4,6,9],4))

def nb_occurrences(lst = list, e = int) -> int :
    """Permet de trouver combien de fois apparait une valeur e dans une liste lst

    Args:
        lst (_type_, optional): _description_. Defaults to list.
        e (_type_, optional): _description_. Defaults to int.

    Returns:
        int: _description_
    """
    nombre = 0
    for i in range (len(lst)) :
        if e == lst[i] :
            nombre += 1
    return nombre

print(nb_occurrences([2,4,3,4,6,9],4))

def est_triee1(lst = list) -> bool :
    e = 0
    i = 1
    for i in range (len(lst)) :
        if e < i :
            triee = True
            e += 1
        else :
            triee = False
            i = len(lst)
    return triee

print(est_triee1([1,2,3,4,5,6]))
print(est_triee1([1,2,3,4,7,6]))