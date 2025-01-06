import random

print("Début de la Bataille")

# 1. Fonction pour créer un jeu de cartes avec des images
def creer_jeu():
    couleurs = ["pique", "carreau", "coeur", "trefle"]
    valeurs = {
        2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept", 
        8: "Huit", 9: "Neuf", 10: "Dix", 11: "Valet", 12: "Dame", 13: "Roi", 
        14: "As"
    }
    
    # Associer une image à chaque carte (chemin fictif)
    jeu = []
    for couleur in couleurs:
        for valeur, nom in valeurs.items():
            image = f"images/{nom}_de_{couleur}.png"  # Exemple de chemin d'image
            jeu.append((couleur, valeur, nom, image))  # Ajouter l'image
    
    return jeu

# 2. Fonction pour mélanger et distribuer les cartes
def melanger_et_distribuer(jeu):
    random.shuffle(jeu)
    joueur_1 = jeu[:26]  # Premier joueur reçoit 26 cartes
    joueur_2 = jeu[26:]  # Deuxième joueur reçoit 26 cartes
    return joueur_1, joueur_2

# 3. Fonction pour simuler une manche de bataille
def bataille(joueur_1, joueur_2):
    score_1, score_2 = 0, 0
    manche = 1  # Numéro de la manche

    # Tant qu'il y a des cartes dans les deux jeux
    while joueur_1 and joueur_2:
        carte_1 = joueur_1.pop(0)
        carte_2 = joueur_2.pop(0)
        
        print(f"Manche {manche}: Joueur 1 a {carte_1[2]} de {carte_1[0]} ({carte_1[3]}), Joueur 2 a {carte_2[2]} de {carte_2[0]} ({carte_2[3]})")
        
        # Comparer les cartes par leur valeur
        if carte_1[1] > carte_2[1]:
            # Joueur 1 gagne la manche
            score_1 += 2
            print("Joueur 1 gagne la manche et prend les cartes.")
        elif carte_1[1] < carte_2[1]:
            # Joueur 2 gagne la manche
            score_2 += 2
            print("Joueur 2 gagne la manche et prend les cartes.")
        else:
            # Égalité, les cartes sont écartées
            print("Égalité, les cartes sont écartées.")
        
        manche += 1  # Passage à la manche suivante

    # Retourner le score final
    return score_1, score_2

# 4. Programme principal
def jeu_bataille():
    # Créer le jeu de cartes
    jeu = creer_jeu()
    
    # Mélanger et distribuer les cartes
    joueur_1, joueur_2 = melanger_et_distribuer(jeu)
    
    # Simuler la bataille
    score_1, score_2 = bataille(joueur_1, joueur_2)
    
    # Afficher les résultats finaux
    print("\n \n  La Bataille est terminée")
    if score_1 > score_2:
        print(f"Joueur 1 gagne la partie avec {score_1} cartes contre {score_2} cartes.")
    elif score_1 < score_2:
        print(f"Joueur 2 gagne la partie avec {score_2} cartes contre {score_1} cartes.")
    else:
        print(f"Égalité avec {score_1} cartes pour chaque joueur.")

# Exécution du jeu
jeu_bataille()
