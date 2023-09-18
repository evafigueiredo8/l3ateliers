import random

def gen_list_random_int(int_binf = 0, int_bsup = 10) -> list:
    """génère une liste de nb aléatoires

    Args:
        int_binf (int, optional): _description_. Defaults to 0.
        int_bsup (int, optional): _description_. Defaults to 10.

    Returns:
        list: _description_
    """
    int_nbr = [0] * 10
    for i in range(len(int_nbr)):
        int_nbr[i] = random.randint(int_binf, int_bsup)
    return int_nbr

def mix_list(list_to_mix: list) -> list:
    """mélange les nb d'une liste et renvoie une nouvelle liste

    Args:
        list_to_mix (list): _description_

    Returns:
        list: _description_
    """
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


# Test de votre code
lst_sorted=gen_list_random_int()

def test_choose(liste):
    """test la fonction choose

    Args:
        liste (_type_): _description_
    """
    print('Liste triée de départ',liste)
    e1 = choose_element_list(liste)
    print('A la première exécution',e1,'a été sélectionné')
    e2 = e1
    while e2 == e1:
        e2 = choose_element_list(lst_sorted)
    print('A la deuxième exécution',e2,'a été sélectionné')
    assert e1 != e2,"Attention vérifiez votre code, pour deux sélections de suite l'élément sélectionné est le même !"

test_choose(lst_sorted)

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

# Test de votre code
print('Liste de départ',lst_sorted)
sublist = extract_elements_list(lst_sorted,5)
print('La sous liste extraite est',sublist)
print('Liste de départ après appel de la fonction est',lst_sorted)