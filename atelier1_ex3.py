import math

def discriminant(a : int,b : int,c : int) -> int :
    """Calcule le discriminant"""
    resultat_d = b*b-4*a*c
    return resultat_d

def racine_unique(a : int,b : int) -> int :
    """Calcule la racine unique"""
    resultat_ru = b*(-1) / 2*a
    return resultat_ru

def racine_double(a : int,b : int,delta : int,num : int) -> int :
    """Calcule la racine double"""
    if num == 1 :
        resultat_rd = (-1 * b + delta**0.5) / 2*a
    elif num == 2 :
        resultat_rd = (-1 * b - delta**0.5) / 2*a
    return resultat_rd

def str_equation(a : int,b : int,c : int) -> str :
    """Affiche l'équation ax2+bx+c=0 en complétant avec les valeurs choisies"""
    valeura = str(a)
    valeurb = str(b)
    valeurc = str(c)

    if a == 0 and b == 0 and c == 0 or a==0 and b==0 :
        resultat = ("0")
    elif a==0 and c==0 :
        resultat = valeurb + "x=0"
    elif b==0 and c==0 :
        resultat = valeura + "x2=0"
    elif b==0 :
        resultat = valeura + "x2+" + valeurc + "=0"
    elif a==0 :
        resultat = valeurb + "x+" + valeurc + "=0"
    elif c==0 :
        resultat = valeura + "x2+" + valeurb + "x=0"
    else :
        resultat = valeura + "x2+" + valeurb + "x+" + valeurc + "=0"

    return resultat

def solution_equation(a : int,b : int,c : int) -> str :
    """Calcule l'équation qui avait été définie avec la fonction au dessus toujours avec les valeurs choisies"""
    chaine_equation = str(str_equation(a,b,c))
    racine_u = str(racine_unique(a,b))
    racine_d1 = str(racine_double(a,b,discriminant(a,b,c),1))
    racine_d2 = str(racine_double(a,b,discriminant(a,b,c),2))

    print("Solution de l'équation " + chaine_equation)
    if discriminant(a,b,c) < 0 :
        resultat = "Pas de racine réelle"
    elif discriminant(a,b,c) == 0 :
        resultat = "Racine unique x=" + racine_u
    else :
        resultat = "Deux racines \nx1 = " + racine_d1 + "\nx2 = " + racine_d2
    return resultat

def equation(a : int,b : int,c : int) :
    """Affiche la solution qui a été calculé au dessus"""
    print(solution_equation(a,b,c))

def test(a : int,b : int,c : int) -> str :
    """Test des fonctions"""
    resultat = equation(a,b,c)
    return resultat

test(5,6,7)
test(1,0,-2)
test(4,1,5)