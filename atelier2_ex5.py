import math

def vitrines(nbEmplacements: int, objets: list):
    if len(objets) > (nbEmplacements*2):
        vitrine1 = [0]*nbEmplacements
        vitrine2 = [0]*nbEmplacements
        for i in range(len(objets)):
            if vitrine1[i] == 0:
                vitrine1[i] = objets[i]
            elif vitrine2[i] == 0:
                vitrine2[i] = objets[i]
    else:
        print("Vous ne pouvez pas avoir plus d'objets que d'emplacements.")
    resultat = ("Pour les entrées nbEmplacement = ",nbEmplacements," et objets = ",objets,", il existe au moins une solution qui est ", vitrine1, vitrine2)
    return resultat

vitrines(4,[1,2,2,3,4,5,5])