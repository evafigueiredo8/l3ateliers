import random
import time
import matplotlib.pyplot as plt
import numpy as np

def gen_list_random_int(nb: int, int_binf = 0, int_bsup = 10) -> list:
    """génère une liste de nb aléatoires

    Args:
        int_binf (int, optional): _description_. Defaults to 0.
        int_bsup (int, optional): _description_. Defaults to 10.

    Returns:
        list: _description_
    """
    int_nbr = [0] * nb
    for i in range(len(int_nbr)):
        int_nbr[i] = random.randint(int_binf, int_bsup)
    return int_nbr

def mix_list(nb: int) -> list:
    """mélange les nb d'une liste et renvoie une nouvelle liste

    Args:
        list_to_mix (list): _description_

    Returns:
        list: _description_
    """
    list_to_mix = gen_list_random_int(nb)
    list_mix = [0] * len(list_to_mix)
    for i in range(len(list_to_mix)):
        aleatoire = random.randint(0,len(list_to_mix)-1)
        list_mix[i] = list_to_mix[aleatoire]
        list_to_mix.pop(aleatoire)
    return list_mix

def choose_element_list(list_in_which_to_choose: list) -> int:
    """choisi un elmt de la liste

    Args:
        list_in_which_to_choose (list): _description_

    Returns:
        int: _description_
    """
    return list_in_which_to_choose[random.randint(0,len(list_in_which_to_choose)-1)]



"""def test_choose(liste):
    =test la fonction choose

    Args:
        liste (_type_): _description_
    
    print('Liste triée de départ',liste)
    e1 = choose_element_list(liste)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = e1
    while e2 == e1:
        e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"""


def extract_elements_list(list_in_which_to_choose: list, nbr_of_element_to_extract : int) -> list:
    """extrait nbr_of_element_to_extract elements de la liste list_in_which_to_choose

    Args:
        list_in_which_to_choose (list): _description_
        nbr_of_element_to_extract (int): _description_

    Returns:
        list: _description_
    """
    liste = [0] * nbr_of_element_to_extract
    for i in range(len(liste)):
        liste[i] = choose_element_list(list_in_which_to_choose)
    return liste


def perf_mix(fonction1: callable, fonction2: callable, liste_tailles: list, nb_exe: int) -> tuple:
    """renvoie un tuple qui calcule la moyenne d'execution de fonctions

    Args:
        fonction1 (callable): fonction list_mix
        fonction2 (callable): fonction shuffle
        liste_tailles (list): _description_
        nb_exe (int): _description_

    Returns:
        tuple: _description_
    """
    #Récupération du temps système et démarrage du chronomètre
    start_pc = time.perf_counter()
    moyenne_f1 = 0
    moyenne_f2 = 0
    liste_moyenne1 = []
    liste_moyenne2 = []
    for e in liste_tailles:
        for i in range(nb_exe):
            fonction1(e)
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moyenne_f1 += elapsed_time_pc
        moyenne_f1 = moyenne_f1/nb_exe
        for i in range(nb_exe):
            fonction2(gen_list_random_int(e))
            end_pc = time.perf_counter()
            elapsed_time_pc = end_pc-start_pc
            moyenne_f2 += elapsed_time_pc
        moyenne_f2 = moyenne_f2/nb_exe
        liste_moyenne1.append(moyenne_f1)
        liste_moyenne2.append(moyenne_f2)
    # Exécutez ce code et vérifiez par vous-même la variabilité des mesures.
    return (liste_moyenne1,liste_moyenne2)

#print(perf_mix(mix_list, random.shuffle,[10,500,5000,50000,100000],10))

def afficher_courbes(liste_moyenne1, liste_moyenne2):
    x_axis_list = [10,500,5000,50000,100000]
    fig, ax = plt.subplots()
    ax.plot(x_axis_list,liste_moyenne1,'bo-',label='Identité')
    ax.plot(x_axis_list,liste_moyenne2, 'r*-', label='Carré')
    ax.set(xlabel='Abscisse x', ylabel='Ordonnée y', title='Comparaison des moyennes')
    ax.legend(loc='upper center', shadow=True, fontsize='x-large')
    plt.show()


l1, l2 = perf_mix(mix_list, random.shuffle,[10,500,5000,50000,100000],10)
print(l1, l2)
afficher_courbes(l1, l2)

#comparer avec la même liste, sortir gen_list_random_int de mix_list pour la fonction 1