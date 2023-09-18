import math

#Question 1

def full_name1(str_arg:str)->str:
    nom_prenom = str_arg.split(" ",1)
    nom_prenom[0]=nom_prenom[0].upper()
    nom_prenom[1]=nom_prenom[1].capitalize()
    return f"{nom_prenom[0]} {nom_prenom[1]}"

print(full_name1("figueiredo eva"))


def full_name2(str_arg:str)->str:
    borne_min = 97
    borne_max = 122
    nom_majuscule = ""
    prenom = ""
    est_nom = True
    for caractere in str_arg:
        ascii_caractere = ord(caractere)
        if caractere == ' ':
            est_nom = False
            est_prenom = True
        elif est_nom:
            if ascii_caractere >= borne_min and ascii_caractere <= borne_max:
                nom_majuscule += chr(ascii_caractere - 32)
            else:
                nom_majuscule += caractere
        elif est_prenom == True:
            if ascii_caractere >= borne_min and ascii_caractere <= borne_max:
                prenom = chr(ascii_caractere - 32)
            else:
                prenom = caractere
            est_prenom = False
        elif prenom != "":
                prenom += caractere
    return f"{nom_majuscule} {prenom}"

print(full_name2("figueiredo eva"))
print(full_name2("figUEiredo Eva"))

#Question 2

def is_mail(str_arg:str)->(int,int):
    valide = True
    arobase = False
    validité = ""
    for i in str_arg:
        if i == "@":
            arobase = True
    if arobase:
        corps, domaine = str_arg.split("@",1)
        for i in corps:
            if corps[0] == "." or corps[-1] == ".":
                valide = False
            elif (i == "." and i-1 == ".") or (i=="." and i+1 == "."):
                valide = False
    else:
        validité = ("(0, 2) le mail n’est pas valide, il manque l’@")
        
    return valide, arobase

print(is_mail("corps..fr"))
