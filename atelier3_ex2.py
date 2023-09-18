import math

def mots_Nlettres(lst_mot: list, n: int) -> list:
    """renvoie la liste des mots contenant exactement n lettres

    Args:
        lst_mot (list): _description_
        n (int): _description_

    Returns:
        list: _description_
    """
    L = []
    for mot in lst_mot:
        if len(mot) == n:
            L.append(mot)
    return L

def commence_par(mot: str, prefixe: str) -> bool:
    """renvoie True si l'argument mot commence par prefixe et False sinon.


    Args:
        mot (str): _description_
        prefixe (str): _description_

    Returns:
        bool: _description_
    """
    i=0
    result = True
    while i < len(prefixe) and result:
        if mot[i] != prefixe[i]:
            result = False
        else:
            i += 1
    return result

def finit_par(mot: str, suffixe: str) -> bool:
    """renvoie True si l'argument mot se termine par suffixe et False sinon.

    Args:
        mot (str): _description_
        suffixe (str): _description_

    Returns:
        bool: _description_
    """
    i= len(mot) - len(suffixe)
    l=0
    result = True
    while i < len(mot) and result:
        if mot[i] != suffixe[l]:
            result = False
        else:
            i += 1
            l += 1
    return result

def finissent_par (lst_mot: list, suffixe: str) -> list:
    """renvoie la liste des mots présents dans la liste lst_mot qui se terminent par suffixe.

    Args:
        lst_mot (list): _description_
        suffixe (str): _description_

    Returns:
        list: _description_
    """
    L = []
    for mot in lst_mot:
        if finit_par(mot, suffixe):
            L.append(mot)
    return L

def commencent_par (lst_mot: list, prefixe: str) -> list:
    """ renvoie la liste des mots présents dans la liste lst_mot qui commencent par prefixe. 

    Args:
        lst_mot (list): _description_
        prefixe (str): _description_

    Returns:
        list: _description_
    """
    L = []
    for mot in lst_mot:
        if commence_par(mot, prefixe):
            L.append(mot)
    return L

def liste_mots(lst_mot: list, prefixe: str, suffixe: str, n: int) -> list:
    return commencent_par(finissent_par(mots_Nlettres(lst_mot,n),suffixe),prefixe)

print(liste_mots(["jouer","bonjour", "punir", "jour", "aurevoir", "revoir", "pouvoir", "cour", "abajour", 
"finir", "aimer"], "e", "our", 8))