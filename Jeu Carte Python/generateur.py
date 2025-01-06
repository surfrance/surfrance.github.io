from PIL import Image, ImageDraw, ImageFont
import os

def creer_repertoire(nom_dossier):
    """Créer un dossier s'il n'existe pas."""
    if not os.path.exists(nom_dossier):
        os.makedirs(nom_dossier)

def generer_cartes():
    """Génère les 52 cartes et les sauvegarde en images."""
    couleurs = ["pique", "carreau", "coeur", "trefle"]
    valeurs = {
        2: "Deux", 3: "Trois", 4: "Quatre", 5: "Cinq", 6: "Six", 7: "Sept",
        8: "Huit", 9: "Neuf", 10: "Dix", 11: "Valet", 12: "Dame", 13: "Roi", 
        14: "As"
    }

    # Créer le répertoire pour les cartes
    dossier_cartes = "cartes_images"
    creer_repertoire(dossier_cartes)

    # Charger la police
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except IOError:
        print("Police non trouvée. Remplacez par une autre disponible.")
        return

    # Générer toutes les cartes
    for couleur in couleurs:
        for valeur, nom in valeurs.items():
            img = Image.new('RGB', (300, 450), color='white')
            draw = ImageDraw.Draw(img)
            texte = f"{nom} de {couleur.capitalize()}"
            w, h = draw.textsize(texte, font=font)
            draw.text(((300 - w) / 2, (450 - h) / 2), texte, fill="black", font=font)
            filename = f"{nom}_de_{couleur}.png"
            img.save(os.path.join(dossier_cartes, filename))

    print("Cartes générées dans le dossier 'cartes_images'.")

if __name__ == "__main__":
    generer_cartes()
