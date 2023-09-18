import math

def separer (L: list) -> list:
    LSEP = []
    rang_dernier_negatif = 0
    for i in range(len(L)):
        if L[i] < 0:
            LSEP.insert(0, L[i])
            rang_dernier_negatif += 1
        elif L[i] > 0:
            LSEP.insert(-1, L[i])
        else:
            LSEP.insert((rang_dernier_negatif+1), L[i])
    return LSEP

print(separer([1,-5,2,0,4,-6,0]))
