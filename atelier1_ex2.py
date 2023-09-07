import math

def est_bissextile(annee : int) -> str :
    bissextile = False
    if annee%4 == 0 and annee%100 != 0 or annee%4 == 400 :
        bissextile = True
    return bissextile

def test_annee(annee : int) -> str:
    if est_bissextile(annee) == True :
        print("L'année est bissextile.")
    else :
        print("L'année n'est pas bissextile.")

test_annee(2020)
test_annee(2023)