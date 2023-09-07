import math

def message_imc (imc : float) -> float :

    IMC = [16.5,18.5,25,30,35,40]
    INTERPRETATION = ["Dénutrition ou famine","Maigreur","Corpulence normale","Surpoids","Obésité modérée","Obésité sévère","Obésité morbide"]

    if imc < IMC[0] :
        interpretation = INTERPRETATION[0]
    elif imc < IMC[1] :
        interpretation = INTERPRETATION[1]
    elif imc < IMC[2] :
        interpretation = INTERPRETATION[2]
    elif imc < IMC[3] :
        interpretation = INTERPRETATION[3]
    elif imc < IMC[4] :
        interpretation = INTERPRETATION[4]
    elif imc < IMC[5] :
        interpretation = INTERPRETATION[5]
    elif imc > IMC[5] :
        interpretation = INTERPRETATION[6]
    
    return interpretation

def test_imc(imc):
    print("L'interprétation de votre IMC est : '" + message_imc(imc) + "'")

test_imc(19)
test_imc(16)