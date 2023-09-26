import math
import random

def places_lettre(ch : str, mot : str) -> list:
    indice = []
    for i in range(len(mot)):
        if ch == mot[i]:
            indice.append(i)
    return indice

def outputStr(mot:str, lpos:list)-> str:
    nvmot = ''
    if lpos == []:
        for i in range(len(mot)):
            nvmot += '-'
    else:
        for pos in range(len(mot)):
            tiret = True
            for indice in range(len(lpos)):
                if lpos[indice] == pos:
                    nvmot += mot[pos]
                    tiret = False
                elif indice == len(lpos)-1 and tiret:
                    nvmot += '-'
    return nvmot


def runGame():
    niveau = input("Choisissez un niveau entre 'easy', 'normal' et 'hard' : ")
    liste = []
    if niveau == "easy":
        for i in range(1,6):
            liste.append(select_word(build_dict(build_list("capitales.txt")),i))
    elif niveau == "normal":
        for i in range(7,8):
            liste.append(select_word(build_dict(build_list("capitales.txt")),i))
    elif niveau == "hard":
        for i in range(8,13):
            liste.append(select_word(build_dict(build_list("capitales.txt")),i))
    else :
        print("Vous devez choisir entre 'easy', 'normal' et 'hard'.")
    mot = random.choice(liste)
    print(outputStr(mot,[]))
    trouve = ''
    nbcoups = 5
    indice = []
    dessins = ["|---]","| O  ","| T  ","|/ \ ","|____"]
    while trouve != mot and nbcoups > 0:
        lettre = input('Entrez une lettre : ')
        indice += places_lettre(lettre,mot)
        trouve = outputStr(mot,indice)
        print(trouve)
        if places_lettre(lettre,mot) == []:
            nbcoups -= 1
            e = nbcoups
            while e >= nbcoups:
                for i in range(5-e):
                    print(dessins[i])
                e -=1
            if nbcoups == 0:
                print("Vous avez perdu !")
            print ("Il vous reste" , nbcoups , "coups.")
    if trouve == mot:
        print("Vous avez gagné !")

def build_list(file : str) -> list:
    file = open(file, "r")
    contenu = file.readlines()
    for i in range(len(contenu)):
        contenu[i] = contenu[i].replace("\n", "")
        contenu[i] = contenu[i].replace("Ã©", "é")
        contenu[i] = contenu[i].replace("Ã¨", "è")
        contenu[i] = contenu[i].lower()
    file.close()
    return contenu

def build_dict(lst: list) -> dict:
    dictionnaire_mots = {}
    for i in lst:
        dictionnaire_mots.update({len(i) : i})
    return dictionnaire_mots

def select_word(sorted_words:dict, word_len:int)->str:
    return sorted_words[word_len]

runGame()