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
    liste = ['bonjour', 'bon', 'maman','table','chemise']
    mot = random.choice(liste)
    print(outputStr(mot,[]))
    i = 4

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
            while nbcoups <= i:
                while e < nbcoups:
                    print(dessins[e])
                    e +=1
                i -= 1
            if nbcoups == 0:
                print("Vous avez perdu !")
            print ("Il vous reste" , nbcoups , "coups.")

'''def build_list(file : str) -> list:
    file = open("capitales.txt", "r")
    contenu = file.readlines()
    file.close()
    liste = contenu.split("\t")
    return liste
    
build_list("capitales.txt")'''

runGame()