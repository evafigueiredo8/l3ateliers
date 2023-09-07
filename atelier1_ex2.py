import math

def est_bissextile(annee : int) -> str :
    bissextile = False
    if annee%4 == 0 :
        bissextile = True
    return bissextile

def test_imc(annee : int) -> str:
    if est_bissextile(annee) == True :
        print("L'année est bissextile.")
    else :
        print("L'année n'est pas bissextile.")

test_imc(2020)
test_imc(2023)
