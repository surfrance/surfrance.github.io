import random
# Définir les valeurs des cartes
valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
valeur_dict = {valeur: index for index, valeur in enumerate(valeurs)}

# Créer un jeu de cartes
def creer_paquet():
    return [(valeur, couleur) for couleur in ['Cœur', 'Carreau', 'Trèfle', 'Pique'] for valeur in valeurs]

# Mélanger et distribuer les cartes
def distribuer_cartes(paquet):
    random.shuffle(paquet)
    return paquet[:len(paquet)//2], paquet[len(paquet)//2:]

# Comparer deux cartes
def comparer_cartes(carte1, carte2):
    valeur1 = carte1[0]
    valeur2 = carte2[0]
    return (valeur_dict[valeur1] > valeur_dict[valeur2]) - (valeur_dict[valeur1] < valeur_dict[valeur2])

# Fonction principale du jeu
def jeu_bataille():
    print("Début du jeu")
    paquet = creer_paquet()
    joueur1, joueur2 = distribuer_cartes(paquet)
    score_joueur1, score_joueur2 = 0, 0

    while joueur1 and joueur2:
        carte1 = joueur1.pop(0)
        carte2 = joueur2.pop(0)
        print(f"Joueur 1 joue: {carte1} - Joueur 2 joue: {carte2}")

        resultat = comparer_cartes(carte1, carte2)
        if resultat > 0:
            score_joueur1 += 1
            print("Joueur 1 gagne la manche !")
        elif resultat < 0:
            score_joueur2 += 1
            print("Joueur 2 gagne la manche !")
        else:
            print("Match nul !")

    print(f"Score final -> Joueur 1: {score_joueur1} | Joueur 2: {score_joueur2}")
    if score_joueur1 > score_joueur2:
        print("Joueur 1 remporte la bataille !")
    elif score_joueur2 > score_joueur1:
        print("Joueur 2 remporte la bataille !")
    else:
        print("Égalité générale !")
# Lancer le jeu
jeu_bataille()
print("Fin du jeu")    
