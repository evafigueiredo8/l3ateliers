import math

def message_imc (imc : float) -> str :
    """Interprétation de l'imc d'une personne"""
    LISTE = [(16.5,"Dénutrition ou famine"),(18.5,"Maigreur"),(25,"Corpulence normale"),(30,"Surpoids"),(35,"Obésité modérée"),(40,"Obésité morbide")]

    for borne, interpretation in LIST :
        if imc < borne :
            resultat = interpretation
      
    if imc < IMC[0] :
        interpretation = INTERPRETATION[0]
    elif imc <= IMC[1] :
        interpretation = INTERPRETATION[1]
    elif imc <= IMC[2] :
        interpretation = INTERPRETATION[2]
    elif imc <= IMC[3] :
        interpretation = INTERPRETATION[3]
    elif imc <= IMC[4] :
        interpretation = INTERPRETATION[4]
    elif imc <= IMC[5] :
        interpretation = INTERPRETATION[5]
    else :
        interpretation = INTERPRETATION[6]
    return resultat

def test_imc(imc):
    print("L'interprétation de votre IMC est : '" + message_imc(imc) + "'")

test_imc(19)
test_imc(16)
