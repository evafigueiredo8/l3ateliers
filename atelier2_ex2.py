import math

def position1(lst: list, elt: int) -> int :
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

def position2(lst: list, elt: int) -> int :
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

def nb_occurrences(lst: list, e: int) -> int :
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

def est_triee1(lst: list) -> bool :
    """Renvoie un bool True si la liste est triée, false si ce n'est pas le cas

    Args:
        lst (list, optional): _description_. Defaults to list.

    Returns:
        bool: True si la liste est triée
    """
    e = 0
    triee = True
    for i in range (1,len(lst)):
        if lst[e] < lst[i] and triee :
            triee = True
            e += 1
        else :
            triee = False
    return triee

print(est_triee1([1,2,3,4,5,6]))
print(est_triee1([4,2,3,4,7,6]))

def est_triee2(lst: list) -> bool :
    """Renvoie un bool True si la liste est triée, false si ce n'est pas le cas

    Args:
        lst (list, optional): _description_. Defaults to list.

    Returns:
        bool: True si la liste est triée
    """
    e = 0
    i = 1
    while i < len(lst) :
        if lst[e] < lst[i] :
            triee = True
            e += 1
            i += 1
        else :
            triee = False
            i = len(lst)
    return triee

print(est_triee2([1,2,3,4,5,6]))
print(est_triee2([4,2,3,4,7,6]))

def position_tri (lst: list, e: int) -> bool :
    """trouve la position d'un élément dans une liste

    Args:
        lst (list): _description_
        e (int): _description_

    Returns:
        bool: renvoie vrai si e fait partie de la liste
    """
    debut = 0
    fin = len(lst)
    trouve = False
    while trouve == False and debut <= fin :
        milieu = (debut + fin)//2
        if lst[milieu] == e :
            trouve = True
        else :
            if e > lst[milieu] :
                debut = milieu + 1
            else :
                fin = milieu - 1
    if trouve == True :
        print("La valeur ", e, " est au rang ", milieu)
    else :
        print("La valeur ", e, " n'est pas dans le tableau.")
    return milieu

print(position_tri([1,2,3,4,5,6], 5))

def a_repetitions(lst: list) -> bool :
    t = []
    repetition = False
    i = 0
    while i < len(lst):
        if lst[i] not in t:
            t.insert(-1, lst[i])
            i += 1
        else:
            i = len(lst) + 1
            repetition = True
    return repetition

print(a_repetitions([1,2,3,4,5,6]))
print(a_repetitions([1,2,3,4,5,5]))