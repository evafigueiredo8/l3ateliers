import math

def discriminant(a : int,b : int,c : int) -> int :
    resultat_d = b*b-4*a*c
    return resultat_d

def test_discriminant(a : int,b : int,c : int) -> str :
    discr = str(discriminant(a,b,c))
    print("Le discriminant est : " + discr)

#test_discriminant(2,1,5)
#test_discriminant(6,1,3)

def racine_unique(a : int,b : int) -> int :
    resultat_ru = b*(-1) / 2*a
    return resultat_ru


def racine_double(a : int,b : int,delta : int,num : int) -> int :
    if num == 1 :
        resultat_rd = (-1 * b + delta**0.5) / 2*a
    elif num == 2 :
        resultat_rd = (-1 * b - delta**0.5) / 2*a
    return resultat_rd
    
def test_double(a : int,b : int,delta : int,num : int) -> str :
    rd = str(racine_double(a,b,delta,num))
    if num == 1 :
        print("La racine double numéro 1 est : " + rd)
    elif num == 2 :
        print("La racine double numéro 2 est : " + rd)
    else :
        print("Il faut entrer 1 ou 2.")

#test_double(6,1,discriminant(2,1,5),1)
#test_double(6,1,discriminant(2,1,5),2)

def str_equation(a : int,b : int,c : int) -> str :
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

#print(str_equation(1,2,3))

def solution_equation(a : int,b : int,c : int) -> str :

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

print(solution_equation(1,2,1))