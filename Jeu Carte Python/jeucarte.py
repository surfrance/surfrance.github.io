import pygame
import pageprincipal

# Initialisation de pygame
pygame.init()

# Créer la fenêtre
pygame.display.set_caption("Duel Des Héros")
screen = pygame.display.set_mode((1100, 615))

# Importer l'arrière-plan
background = pygame.image.load('fond-ecran.png')

# Charger l'image du bouton "Continuer"
button_image = pygame.image.load('bouton/boutoncontinuer.png')
button_rect = button_image.get_rect(center=(550, 400))

# Fonction pour la page principale (à appeler après avoir cliqué sur le bouton "Continuer")
def pageprincipale():
    print("Page principale du jeu")

# Boucle du jeu (pour que la fenêtre reste ouverte)
running = True
while running:
    # Appliquer l'arrière-plan
    screen.blit(background, (0, 0))

    # Afficher le bouton "Continuer"
    screen.blit(button_image, button_rect)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Gestion des événements
    for event in pygame.event.get():
        print(f"Événement détecté: {event}")  # Affiche chaque événement capturé
        # Vérifier si l'utilisateur clique sur le bouton "Continuer"
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):  # Vérifie si le clic est sur l'image du bouton
                print("Clic détecté sur le bouton Continuer")
                pageprincipale()  # Appeler la fonction de la page principale
                running = False  # Fermer la fenêtre actuelle ou vous pouvez la cacher et ouvrir une nouvelle fenêtre

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        
pygame.quit()
