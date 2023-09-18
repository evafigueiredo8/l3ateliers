import math

#Question 1

def histo(F: list) -> list:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        list: _description_
    """
    maxvaleur = 0
    H = []
    for i in range(1, len(F)):
        if F[i] > maxvaleur :
            maxvaleur = F[i]
    for i in range(0,maxvaleur+1):
        H.insert(i,0)
    i = 0
    for i in F:
        H[i] += 1
    return H


def est_injective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    i = 0
    injective = True
    lenH = len(H)
    while i < lenH:
        if H[i] <= 1:
            i += 1
        else:
            injective = False
            i = lenH
    return injective

def est_surjective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    i = 0
    surjective = True
    lenH = len(H)
    while i < lenH:
        if H[i] >= 1:
            i += 1
        else:
            surjective = False
            i = lenH
    return surjective

def est_bijective(F: list) -> bool:
    """_summary_

    Args:
        F (list): _description_

    Returns:
        bool: _description_
    """
    H = histo(F)
    i = 0
    bijective = True
    if est_surjective(F) and est_injective(F):
        bijective = True
    else:
        bijective = False
    return bijective

# Question 2

def val_max (L : list) -> float :
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

def afficheHisto(F: list):
    """_summary_

    Args:
        F (list): _description_
    """
    H = histo(F)
    print(H)
    MAXOCC = val_max(H)
    for i in range(MAXOCC):
        for e in range(len(H)):
            if H[e] >= MAXOCC:
                print("  #" , end ='')
            else:
                print("   ", end ='')
        print("")
        MAXOCC -= 1
    print("|", end ='')
    for e in range(len(H)):
        print("--|", end ='')
    print("")
    for e in range(len(H)):
        print(" ",e, end ='')

afficheHisto([0,1,2,5,5])
