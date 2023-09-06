import math

tariffinal = 0 #float
testtype = True #bool
while testtype :
    typelettre = input("Quel est le type de votre lettre parmi 'v' pour verte, 'p' pour prioritaire ou 'e' pour eco-pli ?").lower()
    if typelettre == "v" or "p" or "e" :
        testtype = False
    else :
        testtype == True

POIDS = [20,100,250,500,1000,3000]
TARIFVERTE = [1.16,2.32,4.00,6.00,7.50,10.50]
TARIFPRIORITAIRE = [1.43,2.86,5.26,7.89,11.44]
TARIFECOPLI = [1.14,2.28,3.92]
poids = input("Quel est le poids de votre lettre en gramme ?" ).math.ceil() #int, converti en entier supérieur le + petit

if typelettre == "v" :
    if poids < POIDS[0] :
        tariffinal = TARIFVERTE[0]
    elif poids < POIDS[1] :
        tariffinal = TARIFVERTE[1]
    elif poids < POIDS[2] :
        tariffinal = TARIFVERTE[2]
    elif poids < POIDS[3] :
        tariffinal = TARIFVERTE[3]
    elif poids < POIDS[4] :
        tariffinal = TARIFVERTE[4]
    elif poids < POIDS[5] :
        tariffinal = TARIFVERTE[5]

if typelettre == "p" :
    if poids < POIDS[0] :
        tariffinal = TARIFPRIORITAIRE[0]
    elif poids < POIDS[1] :
        tariffinal = TARIFPRIORITAIRE[1]
    elif poids < POIDS[2] :
        tariffinal = TARIFPRIORITAIRE[2]
    elif poids < POIDS[3] :
        tariffinal = TARIFPRIORITAIRE[3]
    elif poids < POIDS[5] :
        tariffinal = TARIFPRIORITAIRE[4]

if typelettre == "e" :
    if poids < POIDS[0] :
        tariffinal = TARIFECOPLI[0]
    elif poids < POIDS[1] :
        tariffinal = TARIFECOPLI[1]
    elif poids < POIDS[2] :
        tariffinal = TARIFECOPLI[2]

sticker = input("Voulez-vous un sticker de suivi ? Entrez 'O' pour oui et 'N' pour non")
 # à continuer faire un if et ajouter un prix

print ("Le tarif pour votre lettre est de", tariffinal,"€.")