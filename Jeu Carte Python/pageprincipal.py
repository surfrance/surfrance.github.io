import pygame
import time

# Initialisation de pygame
pygame.init()

# Initialisation de la musique
pygame.mixer.init()  # Nécessaire pour le module mixer

# Charger la musique de fond
pygame.mixer.music.load('Son/open.mp3')  # Remplacez par le nom de votre fichier
pygame.mixer.music.set_volume(0.5)  # Volume
pygame.mixer.music.play(-1)  # Jouer en boucle (-1 pour une boucle infinie)

# Créer la fenêtre
screen = pygame.display.set_mode((1100, 615))
pygame.display.set_caption("Duel Des Héros")

# Importer l'arrière-plan
background = pygame.image.load('fond/fond-ecran.png')

# Charger les images des boutons
button_images = [
    pygame.image.load('bouton/boutonparametre.png'),    # Bouton Paramètre
    pygame.image.load('bouton/boutonmultijoueur.png'),  # Bouton Multijoueur
    pygame.image.load('bouton/boutonjouer.png'),        # Bouton Jouer
    pygame.image.load('bouton/boutonretour.png'),       # Bouton Retour
    pygame.image.load('bouton/boutonquiter.png'),       # Bouton Quitter
    pygame.image.load('bouton/lancerlapartie.png'),     # Bouton Lancer la partie
    pygame.image.load('fond/texte/titre.png')           # Titre
]

# Image de chargement
loading_image = pygame.image.load('fond/fond-ecran-chargement.png')

# Charger l'image du bouton "Continuer"
button_continue_image = pygame.image.load('bouton/boutoncontinuer.png')
button_continue_rect = button_continue_image.get_rect(center=(550, 400))

# Charger l'image du bouton "Retour"
button_retour_image = pygame.image.load('bouton/boutonretour.png')
button_retour_rect = button_retour_image.get_rect(center=(100, 50))

# Positionner les boutons
button_positions = [(150, 100), (150, 200), (150, 300), (150, 400), (150, 500), (850, 450), (700, 150)]
button_rects = [
    button.get_rect(center=pos) for button, pos in zip(button_images, button_positions)
]

# Variables pour suivre l'état actuel
current_box = None

# Fonction pour afficher un encadré
def draw_box(title, content_lines):
    #Affiche un encadré avec un titre et du contenu.
    pygame.draw.rect(screen, (0, 0, 0), (300, 50, 700, 500))  # Fond noir de l'encadré
    pygame.draw.rect(screen, (255, 255, 255), (300, 50, 700, 500), 3)  # Bordure blanche

    font_title = pygame.font.Font(None, 50)
    font_content = pygame.font.Font(None, 30)

    # Afficher le titre
    title_text = font_title.render(title, True, (255, 255, 255))
    screen.blit(title_text, (350, 70))  # Positionner le titre

    # Afficher le contenu ligne par ligne
    for i, line in enumerate(content_lines):
        content_text = font_content.render(line, True, (255, 255, 255))
        screen.blit(content_text, (320, 150 + i * 40))  # Ajuster la position ligne par ligne

# Page de chargement
def page_de_chargement():
    #Affiche une page de chargement pendant 10 secondes avant de passer à la page de jeu.
    start_time = time.time()
    loading_duration = 5  # Durée en secondes
    running = True

    # Titre
    button_continue_image = pygame.image.load('fond/texte/titre.png')
    button_continue_rect = button_continue_image.get_rect(center=(550, 200))


    while running:
        # Appliquer un fond ou une image de chargement
        screen.fill((0, 0, 0))  # Fond noir
        screen.blit(loading_image, (0, 0))  # Position de l'image
        

        # Afficher une barre de progression
        elapsed_time = time.time() - start_time
        progress_width = int((elapsed_time / loading_duration) * 600)  # Barre de progression
        pygame.draw.rect(screen, (255, 255, 255), (250, 500, 600, 20))  # Fond de la barre
        pygame.draw.rect(screen, (0, 0, 0), (250, 500, progress_width, 20))  # Barre remplie
        screen.blit(button_continue_image, button_continue_rect)

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Vérifie si le temps de chargement est écoulé
        if elapsed_time >= loading_duration:
            running = False  # Quitter la boucle

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

# Page de jeu
def page_de_jeu():
    """Affiche la page principale du jeu après le chargement."""
    running = True

    papier_image = pygame.image.load('papier2.png')
    papier_rect = papier_image.get_rect(center=(620, 300))

    score_image = pygame.image.load('fond/texte/score.png')
    score_rect = score_image.get_rect(center=(350, 50))

    gagnant_image = pygame.image.load('fond/texte/gagnant.png')
    gagnant_rect = gagnant_image.get_rect(center=(750, 80))

    # Chargement du bouton "info"
    button_info_image = pygame.image.load('bouton/boutoninfo.png') 
    button_info_rect = button_info_image.get_rect(center=(100, 100))  

    # Variables pour afficher l'encadré d'informations
    encadre_info = False  # Variable pour savoir si l'encadré doit être affiché
    font = pygame.font.Font(None, 6)  # Police pour le texte d'informations


    while running:
        # Appliquer l'arrière-plan
        screen.blit(background, (0, 0))
        screen.blit(button_retour_image, button_retour_rect)
        font = pygame.font.Font(None, 74)
        text = font.render("jeu !", True, (255, 255, 255))
        screen.blit(text, (300, 100))
        screen.blit(papier_image, papier_rect)
        screen.blit(score_image, score_rect)
        screen.blit(gagnant_image, gagnant_rect)
        screen.blit(button_info_image, button_info_rect)

        # Si l'encadré d'informations doit être affiché, dessinez-le
        if encadre_info:
            # Dessiner un encadré avec une couleur de fond
            encadre_rect = pygame.Rect(215, 35, 800, 450)  # Rect de l'encadré
            pygame.draw.rect(screen, (0, 0, 0), encadre_rect)  # Fond blanc
            pygame.draw.rect(screen, (255, 255, 255), encadre_rect, 3)  # Bordure noire

            # Texte d'informations
            info_text = font.render("Voici les informations du jeu : ", True, (255, 255, 255))
            screen.blit(info_text, (250, 70))

            # Exemple de texte supplémentaire
            details_text = font.render("Ce jeu consiste à résoudre des puzzles !", True, (0, 0, 0))
            screen.blit(details_text, (160, 210))

            details_text2 = font.render("Bonne chance !", True, (0, 0, 0))
            screen.blit(details_text2, (160, 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_retour_rect.collidepoint(event.pos):
                    page_principale()
                    running = False
             # Si le bouton "info" est cliqué
                if button_info_rect.collidepoint(event.pos):
                    encadre_info = not encadre_info  # Afficher/masquer l'encadré d'informations


# Mise à jour de la page principale pour inclure la transition vers le chargement
def page_principale():
    global current_box
    running = True

    while running:
        # Appliquer l'arrière-plan
        screen.blit(background, (0, 0))

        # Afficher tous les boutons du menu principal
        for i, button in enumerate(button_images):
            screen.blit(button, button_rects[i])

        # Afficher l'encadré actuel si nécessaire
        if current_box == "parametre":
            draw_box("Paramètres", ["Option 1: Volume", "Option 2: Commandes", "Option 3: Graphismes"])
        elif current_box == "multijoueur":
            draw_box("Multijoueur", ["Jouez en ligne avec vos amis !"])
        elif current_box == "jouer":
            draw_box("Jouer", ["Choisissez votre mode de jeu"])
        elif current_box == "Retour":
            draw_box("Retour", ["Utilisez les flèches pour naviguer.", "Appuyez sur ESC pour revenir."])
        elif current_box == "quitter":
            draw_box("Quitter", ["Voulez-vous vraiment quitter ?", "", "Si vous quittez, toute votre progression sera", "définitivement supprimée !", "", "Cliquez sur la croix en haut à droite."])

        # Mettre à jour l'affichage
        pygame.display.flip()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i, rect in enumerate(button_rects):
                    if rect.collidepoint(event.pos):  # Si le clic est sur un bouton
                        if i == 0:
                            current_box = "parametre"  # Afficher les paramètres
                        elif i == 1:
                            current_box = "multijoueur"  # Afficher le multijoueur
                        elif i == 2:
                            current_box = "jouer"  # Afficher les modes de jeu
                        elif i == 3:
                            current_box = "retour"  # Faire retour
                        elif i == 4:
                            current_box = "quitter"  # Afficher le menu quitter
                        elif i == 5:  # Bouton "Lancer la partie"
                            page_de_chargement()
                            page_de_jeu()
                            running = False

# Fonction d'accueil
def accueil():
    running = True

    while running:
        screen.blit(background, (0, 0))
        screen.blit(button_continue_image, button_continue_rect)
        font = pygame.font.Font(None, 74)
        text = font.render("Le Duel des Héros", True, (0, 0, 0))
        screen.blit(text, (300, 200))
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_continue_rect.collidepoint(event.pos):
                    page_principale()
                    running = False

# Lancer l'application
if __name__ == "__main__":
    accueil()
