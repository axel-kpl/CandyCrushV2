from functions_mat import *
import matplotlib.pyplot as plt


#                        .__      ___.   .__
#    ___  _______ _______|__|____ \_ |__ |  |   ____
#    \  \/ /\__  \\_  __ \  \__  \ | __ \|  | _/ __ \
#     \   /  / __ \|  | \/  |/ __ \| \_\ \  |_\  ___/
#      \_/  (____  /__|  |__(____  /___  /____/\___  >
#                \/              \/    \/          \/

taille_totale = 8
couleurs = [
    "#FF9100",
    "#FF0000",
    "#498100",
    "#1700B0",
    "#FFFFFF",
]  # ne pas rajouter de couleurs !!! Les 4 premieres
# sont les couleurs des bonbons, la dernière est la couleur de disparition des bonbons
delay = 0.2  # delai en seconde !!
labels_grille = [
    [None for _ in range(taille_totale)] for _ in range(taille_totale)
]  # Stocke les widgets


# ON GENERE LE MONDE

user_choice = int(input("Voulez vous importer un jeu ou creer un jeu random ? 1/2 : "))
while user_choice != 1 and user_choice != 2:
    user_choice = int(
        input("Voulez vous importer un jeu ou creer un jeu random ? 1/2 : ")
    )
if user_choice == 1:
    fichier_nom = input("Quel est le nom de votre fichier a importer ? : ")
    if ".csv" not in fichier_nom:
        fichier_nom += ".csv"
    modele_raw = extraire_csv(fichier_nom, True)
    taille_totale = 7  # ne pas modifier ici, gestion de l'import csv
else:
    modele_raw = creer_monde_random(4, taille_totale)
    while (test_alignement(modele_raw) != []) or (not prevision(modele_raw)):
        modele_raw = creer_monde_random(4, taille_totale)


start_affichage(taille_totale, couleurs, modele_raw, delay)
