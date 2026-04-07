from functions_mat import *
import matplotlib.pyplot as plt
import os


#                        .__      ___.   .__
#    ___  _______ _______|__|____ \_ |__ |  |   ____
#    \  \/ /\__  \\_  __ \  \__  \ | __ \|  | _/ __ \
#     \   /  / __ \|  | \/  |/ __ \| \_\ \  |_\  ___/
#      \_/  (____  /__|  |__(____  /___  /____/\___  >
#                \/              \/    \/          \/

taille_totale = 7
banque = ["#FF9100", "#FF0000", "#498100", "#1700B0", "#AE00B0", "#A33939", "#000000"]
couleur_dis = "#FFFFFF"  # ne pas rajouter de couleurs !!! Les premieres
# sont les couleurs des bonbons, la dernière est la couleur de disparition des bonbons
delay = 0.2  # delai en seconde !!
labels_grille = [
    [None for _ in range(taille_totale)] for _ in range(taille_totale)
]  # Stocke les widgets
score = [0]

# ON GENERE LE MONDE

print(r"  ____    _    _   _  ____ __   __     ____ ____  _   _ ____  _   _ ")
print(r" / ___|  / \  | \ | ||  _ \\\\ \ / /    / ___|  _ \| | | / ___|| | |")
print(r"| |     / _ \ |  \| || | | |\ V /    | |   | |_) | | | \___ \| |_| |")
print(r"| |___ / ___ \| |\  || |_| | | |     | |___|  _ <| |_| |___) |  _  |")
print(r" \____/_/   \_\_| \_||____/  |_|      \____|_| \_\\___/|____/|_| |_|")
print("Bienvenue sur le jeu CandyCrush ! ")
print("Pour plus d'info, allez voir sur github !")
print("\n")
user_difficulty = input("Choisir la difficulté (1/2) : ")
while user_difficulty != "1" and user_difficulty != "2":
    user_difficulty = input("Choisir la difficulté (1/2) : ")
if user_difficulty == "2":
    niveau2 = True
else:
    niveau2 = False
user_color = int(input("Choissisez le nombre n de couleurs (entre 3 et 7) : "))
while user_color < 3 or user_color > 7:
    user_color = int(input("Choissisez le nombre n de couleurs (entre 3 et 7) : "))
couleurs = banque[:user_color] + [couleur_dis]
user_choice = int(input("Voulez vous importer un jeu ou creer un jeu random ? 1/2 : "))
while user_choice != 1 and user_choice != 2:
    user_choice = int(
        input("Voulez vous importer un jeu ou creer un jeu random ? 1/2 : ")
    )
if user_choice == 1:
    fichier_nom = input("Quel est le nom de votre fichier a importer ? : ")
    if ".csv" not in fichier_nom:
        fichier_nom += ".csv"
        dossier_actuel = os.path.dirname(os.path.abspath(__file__))
        chemin_complet = os.path.join(dossier_actuel, fichier_nom)
        # ne pas modifier ici, gestion de l'import csv
        modele_raw = extraire_csv(chemin_complet, True)
        taille_totale = len(modele_raw)

else:
    modele_raw = creer_monde_random(len(couleurs) - 1, taille_totale)
    while (test_alignement(modele_raw, niveau2) != []) or (
        not prevision(modele_raw, niveau2)
    ):
        modele_raw = creer_monde_random(5, taille_totale)


start_affichage(taille_totale, couleurs, modele_raw, delay, niveau2, score)
