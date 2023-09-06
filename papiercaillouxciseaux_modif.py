import random

question = input("Voulez-vous jouer contre l'ordinateur (Max 5 parties) O/N ?" )
if question != 'O' and question != 'N' :
        print("Je n'ai pas compris votre réponse")
else :
    nom1 = input("Quel est votre nom ?")
    print("Bienvenu",nom1,"nous allons jouer ensemble \n")
    if question == 'O':
        nom2 = 'Machine'
    else :
        nom2 = input("Quel est le nom du deuxième joueur ?")
    print("Bienvenu",nom2, "nous allons jouer ensemble \n")

score1 = 0
score2 = 0
nbmanche = 0
jouer = True

while jouer == True:
    nbmanche += 1
    reponse1 = input("{nom} faîtes votre choix parmi (pierre, papier, ciseaux, ): ".format(nom=nom1))
    if reponse1 != 'pierre' and reponse1 != 'feuille' and reponse1 != 'ciseaux':
            testreponse1 = False
            print("Je n'ai pas compris votre réponse")
            while testreponse1 == False :
                print("Joueur ", nom1)
                reponse1 = input(" faîtes votre choix parmi (pierre, feuille, ciseaux, ): ")
                testreponse1 = True
                if reponse1 != 'pierre' and reponse1 != 'feuille' and reponse1 != 'ciseaux':
                    testreponse1 = False

    if question == 'O' :
        reponse2 = ['feuille','pierre','ciseaux', ][random.randint(0, 2)]

    if question == 'N':
        print("Joueur", nom2)
        reponse2 = input("faîtes votre choix parmi (pierre, feuille, ciseaux, ): ")
        if reponse2 != 'pierre' and reponse2 != 'feuille' and reponse2 != 'ciseaux' :
            testreponse2 = False
            print("Je n'ai pas compris votre réponse")
            while not testreponse2 :
                print("Joueur ", nom2)
                reponse2 = input(" faîtes votre choix parmi (pierre, feuille, ciseaux, ): ")
                testreponse2 = True
                if reponse2 != 'pierre' and reponse2 != 'feuille' and reponse2 != 'ciseaux' :
                    testreponse2 = False

    #On affiche les choix de chacun
    print("Si on récapitule :",nom1, reponse1, "et", nom2, reponse2,"\n")


    #On regarde qui a gagné cette manche on calcule les points et on affiche le résultat

    if reponse1 == reponse2 :
        gagnant = "aucun de vous, vous être ex æquo"
    elif reponse1 == 'pierre' and reponse2 == 'feuille' or reponse1 == 'feuille' and reponse2 == 'ciseaux' or reponse1 == 'ciseaux' and reponse2 == 'pierre':
        gagnant = nom2
        score2 = score2 + 1
    else :
        gagnant = nom1
        score1 = score1 + 1

    print("le gagnant est",gagnant)
    print("Les scores à l'issue de cette manche sont donc",nom1, score1, "et", nom2, score2, "\n")

    if nbmanche >= 1 and nbmanche <= 4:
        jouer = True
    if nbmanche ==5:
        jouer = False
        
    if nbmanche ==1 or nbmanche ==2 or nbmanche==3 or nbmanche==4:
        #On propose de continuer ou de s'arrêter 
        continuer = input("Souhaitez vous refaire une partie {} contre {} ? (O/N) ".format(nom1,nom2))
        if continuer == 'O':
            jouer = True
        elif continuer != 'O' and continuer != 'N':
            jouer = True
            print("Vous ne répondez pas à la question, on continue")
        else :
            print("Merci d'avoir joué ! A bientôt")