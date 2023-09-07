import math

def est_bissextile(annee : int) -> str :
    """Calcule si c'est une année bissextile ou non"""
    bissextile = False
    if annee%4 == 0 and annee%100 != 0 or annee%4 == 400 :
        bissextile = True
    return bissextile

def test_annee(annee : int) -> str:
    """Test la fonction est_bissextile"""
    if est_bissextile(annee) == True :
        print("L'année est bissextile.")
    else :
        print("L'année n'est pas bissextile.")

test_annee(2020)
test_annee(2023)