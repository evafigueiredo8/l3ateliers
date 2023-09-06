import math

tarif = 0 #float
testtype = True #bool
while testtype :
    typelettre = input("Quel est le type de votre lettre parmi 'v' pour verte, 'p pour prioritaire ou 'e' pour eco-pli ?").lower()
    if typelettre == "v" or "p" or "e" :
        testtype = False
    else :
        testtype == True

POIDS = [20,100,250,500,1000,3000]
poids = input("Quel est le poids de votre lettre en gramme ?" ).math.ceil() #int, converti en entier supérieur le + petit

if typelettre == "v" :
    if poids < POIDS(0) :
        tarif = 1.16
    elif poids < POIDS(1) :
        tarif = 2.32
    elif poids < POIDS(2) :
        tarif = 4.00
    elif poids < POIDS(3) :
        tarif = 6.00
    elif poids < POIDS(4) :
        tarif = 7.50
    elif poids < POIDS(5) :
        tarif = 10.50

if typelettre == "p" :
    if poids < POIDS(0) :
        tarif = 1.43
    elif poids < POIDS(1) :
        tarif = 2.86
    elif poids < POIDS(2) :
        tarif = 5.26
    elif poids < POIDS(3) :
        tarif = 7.89
    elif poids < POIDS(5) :
        tarif = 11.44

if typelettre == "e" :
    if poids < POIDS(0) :
        tarif = 1.14
    elif poids < POIDS(1) :
        tarif = 2.28
    elif poids < POIDS(2) :
        tarif = 3.92

print ("Le tarif pour votre lettre est de", tarif,"€.")