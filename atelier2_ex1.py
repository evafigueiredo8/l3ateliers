import math

def somme1(L = list) -> int :
    """Fonction qui utilise la boucle for et range

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        int: _description_
    """
    somme = 0
    for i in range (len(L)) :
        somme += L[i]
    return somme

def somme2(L = list) -> int :
    """Fonction qui utilise la boucle for et in

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        int: _description_
    """
    somme = 0
    for i in L :
        somme += i
    return somme

def somme3(L = list) -> int :
    """Fonction qui utilise la boucle while

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        int: _description_
    """
    somme = 0
    i=0 #int
    while i<len(L) :
        somme += L[i]
        i += 1
    return somme

'''La version while me parrait être la plus adaptée car on ne connait pas le nombre de valeurs dans la liste L'''

def test1_exercice1 ():
    '''Fonction qui permet de tester les fonctions de somme'''
    print("TEST SOMME")
    #test liste vide
    print("Test liste vide : ", somme1([]))
    print("Test liste vide : ", somme2([]))
    print("Test liste vide : ", somme3([]))
    #test somme 11111
    lst2test1=[1,10,100, 1000,10000]
    print("Test somme 11111 : ", somme1(lst2test1))
    print("Test somme 11111 : ", somme2(lst2test1))
    print("Test somme 11111 : ", somme3(lst2test1))

test1_exercice1 ()

def moyenne(L = list) -> float :
    """Fonction qui utilise la boucle while

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        float: _description_
    """
    moyenne = 0 # float
    if L != [] :
        i=0 #int
        while i<len(L) :
            moyenne += L[i]
            i += 1
        moyenne = moyenne / len(L)
    return moyenne

def test2_exercice1 ():
    '''Fonction qui permet de tester les fonctions de moyenne'''
    print("TEST MOYENNE")
    #test liste vide
    print("Test liste vide : ", moyenne([]))
    #test moyenne
    lst2test1=[1,10,100, 1000,10000]
    print("Test moyenne : ", moyenne(lst2test1))

test2_exercice1 ()

def nb_sup1 (L = list,e = int) -> int :
    """Fonction qui permet de recup le nb de valeurs supérieures à e dans la liste L avec for range

    Args:
        L (_type_, optional): _description_. Defaults to list.
        e (_type_, optional): _description_. Defaults to int.

    Returns:
        int: _description_
    """
    nombre = 0 # int
    for i in range (len(L)) :
        if e < L[i] :
            nombre += 1
    return nombre

def nb_sup2 (L = list,e = int) -> int :
    """Fonction qui permet de recup le nb de valeurs supérieures à e dans la liste L avec for in

    Args:
        L (_type_, optional): _description_. Defaults to list.
        e (_type_, optional): _description_. Defaults to int.

    Returns:
        int: _description_
    """
    nombre = 0 # int
    for i in L :
        if e < i :
            nombre += 1
    return nombre

def test3_exercice1 ():
    '''Fonction qui permet de tester les fonctions de nb sup'''
    print("TEST NOMBRES SUPERIEURS")
    #test liste vide
    print("Test nb supérieurs : ", nb_sup1([],0))
    print("Test nb supérieurs : ", nb_sup2([],0))
    #test nb sup
    lst2test1=[1,10,100,1000,10000] # list
    print("Test nb supérieurs : ", nb_sup1(lst2test1, 15))
    print("Test nb supérieurs : ", nb_sup2(lst2test1, 15))

test3_exercice1 ()

def moy_sup (L = list,e = int) -> float :
    """Fonction qui permet de calculer la moyenne des nb de valeurs supérieures à e dans la liste L

    Args:
        L (_type_, optional): _description_. Defaults to list.
        e (_type_, optional): _description_. Defaults to int.

    Returns:
        float: moyenne des nb sup
    """
    moyenne_sup = 0 # int
    liste_sup = []
    if L:
        for i in L :
            if e < i :
                liste_sup.append(i)
                moyenne_sup += i
        if liste_sup :
            moyenne_sup = moyenne(liste_sup)
    return moyenne_sup

def test4_exercice1 ():
    '''Fonction qui permet de tester les fonctions de moyenne des nb sup'''
    print("TEST MOYENNE NOMBRES SUPERIEURS")
    #test liste vide
    print("Test moyenne nb supérieurs : ", moy_sup([],0))
    #test moyenne nb sup
    lst2test1=[1,10,100,1000,10000] # list
    print("Test moyenne nb supérieurs : ", moy_sup(lst2test1, 15))

test4_exercice1 ()

def val_max (L = list) -> float :
    """Fonction qui permet de trouver la valeur maximale de la liste

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        float: _description_
    """
    valeur = 0 # int
    for i in L :
        if valeur < i :
            valeur = i
    return valeur

def test5_exercice1 ():
    '''Fonction qui permet de tester les fonctions de valeur max'''
    print("TEST VALEUR MAX")
    #test liste vide
    print("Test valeur max : ", val_max([]))
    #test valeur sup
    lst2test1=[1,10,100,1000,10000] # list
    print("Test valeur max : ", val_max(lst2test1))

test5_exercice1 ()

def ind_max (L = list) -> float :
    """Fonction qui permet de trouver l'indice du nb max de la liste

    Args:
        L (_type_, optional): _description_. Defaults to list.

    Returns:
        float: _description_
    """
    indice = 0 # int
    for i in range (len(L)) :
        if L[i] == val_max (L) :
            indice = i
    return indice

def test6_exercice1 ():
    '''Fonction qui permet de tester la fonction d'indice max'''
    print("TEST INDICE MAX")
    #test liste vide
    print("Test indice max : ", ind_max([]))
    #test indice max
    lst2test1=[1,10,100,1000,10000] # list
    print("Test indice max : ", ind_max(lst2test1))

test6_exercice1 ()