import math

def position(lst = list,elt = int) -> int :
    indice = -1
    for i in range (len(lst)) :
        if elt == lst[i] :
            indice = i
    return indice

print(position([2,5,3,4,6,9],4))