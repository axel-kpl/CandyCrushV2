from functions import *
from tkinter import ttk


#                        .__      ___.   .__
#    ___  _______ _______|__|____ \_ |__ |  |   ____
#    \  \/ /\__  \\_  __ \  \__  \ | __ \|  | _/ __ \
#     \   /  / __ \|  | \/  |/ __ \| \_\ \  |_\  ___/
#      \_/  (____  /__|  |__(____  /___  /____/\___  >
#                \/              \/    \/          \/

taille_totale = 8
couleurs = ["#FF0066", "#FF00D9", "#870DEB", "#FF0084"]

premier_clic = [None]  # Stockera (ligne, colonne) du premier pion choisi
labels_grille = [
    [None for _ in range(taille_totale)] for _ in range(taille_totale)
]  # Stocke les widgets

# ON GENERE LE MONDE

modele_raw = creer_monde_random(4, taille_totale)
while (test_alignement(modele_raw) != []) or (not prevision(modele_raw)):
    modele_raw = creer_monde_random(4, taille_totale)


start_affichage(taille_totale, couleurs, modele_raw, labels_grille, premier_clic)
