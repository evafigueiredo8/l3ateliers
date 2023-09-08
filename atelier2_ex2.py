import math

def position1(lst = list,elt = int) -> int :
    indice = -1
    for i in range (len(lst)) :
        if elt == lst[i] :
            indice = i
    return indice

print(position1([2,5,3,4,6,9],4))

def position2(lst = list,elt = int) -> int :
    indice = -1
    i = 0
    while elt != lst[i] :
        i += 1
    if elt == lst[i] :
        indice = i
    return indice

print(position2([2,5,3,4,6,9],4))