import math

def somme1(L = list) -> int : 
    '''Fonction qui utilise la boucle for et range'''
    somme = 0

    for i in range (len(L)) :
        somme += L[i]

    return somme

def somme2(L = list) -> int :
    '''Fonction qui utilise la boucle for et in'''
    somme = 0

    for i in L :
        somme += i

    return somme

def somme3(L = list) -> int :
    '''Fonction qui utilise la boucle while'''
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
    '''Fonction qui utilise la boucle while'''
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

def nb_sup (L = list,e = int) -> int :

    nombre = 0 # int

    for i in range (len(L)) :
        if e < L[i] :
            nombre += 1

    return nombre

def nb_sup (L = list,e = int) -> int :

    nombre = 0 # int

    for i in L :
        if e < i :
            nombre += 1

    return nombre

def test3_exercice1 ():
    '''Fonction qui permet de tester les fonctions de moyenne'''
    print("TEST NOMBRES SUPERIEURS")
    #test liste vide
    print("Test nb supérieurs : ", nb_sup([],0))
    #test nb sup
    lst2test1=[1,10,100,1000,10000] # list
    print("Test moyenne : ", nb_sup(lst2test1, 15))

test3_exercice1 ()

def moy_sup (L = list,e = int) -> float :
    moyenne_sup = 0 # int
    liste_sup = []

    if L != [] :
        i=0 #int
        while i<len(L) :
            if e < i :
                liste_sup += i
                moyenne_sup += L[i]
            i += 1
        moyenne_sup = moyenne_sup / len(L)

    return moyenne_sup

def test4_exercice1 ():
    '''Fonction qui permet de tester les fonctions de moyenne'''
    print("TEST MOYENNE NOMBRES SUPERIEURS")
    #test liste vide
    print("Test moyenne nb supérieurs : ", moy_sup([],0))
    #test moyenne nb sup
    lst2test1=[1,10,100,1000,10000] # list
    print("Test moyenne nb supérieurs : ", moy_sup(lst2test1, 15))

test4_exercice1 ()