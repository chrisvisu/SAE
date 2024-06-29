import csv
def lire_fichier_csv(base_donnees):
    liste_contenu = []  # Créer une liste vide pr stocker le contenu du fichier CSV
    # Ouvrir le fichier CSV
    with open(base_donnees, 'r') as fichier_csv:
        # Lire chaque ligne du fichier CSV
        for ligne in fichier_csv:
            # Diviser la ligne en une liste d'éléments en utilisant la virgule comme séparateur
            elements = ligne.strip().split(';')
            # Ajouter la liste d'éléments à la liste principale
            liste_contenu.append(elements)
            

    return liste_contenu
#______________________________________________________________________________________________________


# Appeler la fonction pour lire le fichier CSV
base_donnees = r"C:\iut\ccbc_.csv"
recipes:list = lire_fichier_csv(base_donnees)
#print(recipes)

def trouver_recettes(donnees, mots):
    # Convertir les mots en minuscules pour une comparaison insensible à la casse
    mots = [mot.lower() for mot in mots]
    # Liste pour stocker les recettes correspondantes
    recettes_correspondantes = []
    
    # Itérer à travers chaque sous-liste de recette
    for recette in donnees[1:]:  # Sauter l'en-tête
        # Combiner tous les éléments de la sous-liste en une seule chaîne
        recette_combinee = " ".join(recette).lower()
        # Vérifier si tous les mots sont dans la chaîne combinée
        if all(mot in recette_combinee for mot in mots):
            recettes_correspondantes.append(recette)
    
    return recettes_correspondantes



# Demander à l'utilisateur de taper cinq mots
mots_entree = []
for i in range(5):
    mot = input(f"Entrez le mot {i+1}: ")
    mots_entree.append(mot)

# Trouver et imprimer les recettes correspondantes
recettes_correspondantes = trouver_recettes(recipes, mots_entree)
for recette in recettes_correspondantes:
    print("Vous pouvez preparer avec vos ingredient:")
    print(recette)

