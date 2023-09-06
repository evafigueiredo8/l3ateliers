import math

tarif = 0 #float
testtype = True #bool
while testtype :
    typelettre = input("Quel est le type de votre lettre parmi 'verte', 'prioritaire' ou 'éco-pli' ?" )
    if typelettre == "verte" or "prioritaire" or "éco-pli" :
        testtype = False
    else :
        testtype == True


poids = input("Quel est le poids de votre lettre en gramme ?" ) #int

if typelettre == "verte" :
    if poids < 20 :
        tarif = 1.16
    elif poids < 100 :
        tarif = 2.32
    elif poids < 250 :
        tarif = 4.00
    elif poids < 500 :
        tarif = 6.00
    elif poids < 1000 :
        tarif = 7.50
    elif poids < 3000 :
        tarif = 10.50

if typelettre == "prioritaire" :
    if poids < 20 :
        tarif = 1.43
    elif poids < 100 :
        tarif = 2.86
    elif poids < 250 :
        tarif = 5.26
    elif poids < 500 :
        tarif = 7.89
    elif poids < 3000 :
        tarif = 11.44

if typelettre == "éco-pli" :
    if poids < 20 :
        tarif = 1.14
    elif poids < 100 :
        tarif = 2.28
    elif poids < 250 :
        tarif = 3.92
