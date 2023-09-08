import math

def somme1(L) -> int : #L de type liste
    '''Fonction qui utilise la boucle for et range'''
    somme = 0

    for i in range (len(L)) :
        somme += L[i]

    return somme

def somme2(L) -> int : #L de type liste
    '''Fonction qui utilise la boucle for et in'''
    somme = 0

    for i in L :
        somme += i

    return somme

def somme3(L) -> int : #L de type liste
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

def moyenne(L) -> int : #L de type liste
    '''Fonction qui utilise la boucle while'''
    moyenne = 0
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