from functions import *
from tkinter import ttk
import os


#                        .__      ___.   .__
#    ___  _______ _______|__|____ \_ |__ |  |   ____
#    \  \/ /\__  \\_  __ \  \__  \ | __ \|  | _/ __ \
#     \   /  / __ \|  | \/  |/ __ \| \_\ \  |_\  ___/
#      \_/  (____  /__|  |__(____  /___  /____/\___  >
#                \/              \/    \/          \/

taille_totale = 8
couleurs = ["#FF0000", "#55FF00", "#FFFB00", "#0400FF", "#000000"]
delay = 600
premier_clic = [None]  # Stockera (ligne, colonne) du premier pion choisi
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
        dossier_actuel = os.path.dirname(os.path.abspath(__file__))
        chemin_complet = os.path.join(dossier_actuel, fichier_nom)
        taille_totale = 7  # ne pas modifier ici, gestion de l'import csv
        modele_raw = extraire_csv(chemin_complet, True)
else:
    modele_raw = creer_monde_random(4, taille_totale)
    while (test_alignement(modele_raw) != []) or (not prevision(modele_raw)):
        modele_raw = creer_monde_random(4, taille_totale)


start_affichage(taille_totale, couleurs, modele_raw, labels_grille, premier_clic, delay)
