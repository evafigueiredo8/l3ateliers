import math

def est_bissextile(annee : int) -> str :
    """Calcule si c'est une année bissextile ou non"""
    bissextile = False
    if annee%4 == 0 and annee%100 != 0 or annee%4 == 400 :
        bissextile = True
    return bissextile

def date_est_valide(jour : int, mois : int, annee : int) -> bool :
    """Calcule si c'est une année bissextile ou non"""

    JOUR = [28,29,30,31]
    MOIS31 = [1,3,5,7,9,11]
    MOIS30 = [4,6,8,10,12]

    jour_valide = False
    if mois == 2 :
        bissextile = est_bissextile(annee)
        if bissextile and jour == JOUR[1] or bissextile == False and jour == JOUR[0] :
            jour_valide = True
    elif mois in MOIS31 and jour == JOUR[3] or mois in MOIS30 and jour == JOUR[2]:
            jour_valide = True

    return jour_valide

def est_bissextile(annee : int) -> str :
    """Calcule si c'est une année bissextile ou non"""
    bissextile = False
    if annee%4 == 0 and annee%100 != 0 or annee%4 == 400 :
        bissextile = True
    return bissextile


    