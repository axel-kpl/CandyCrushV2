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
banque = [
    "#FF9100",
    "#FF0000",
    "#498100",
    "#1700B0",
    "#AE00B0",
    "#A33939",
    "#000000",
]  # NE PAS TOUCHER AUX COULEURS !!
couleur_dis = "#FFFFFF"
delay = 0.2  # delai en seconde !!
labels_grille = [
    [None for _ in range(taille_totale)] for _ in range(taille_totale)
]  # Stocke les widgets
score = [0]


def lancer_partie(diff_val, mode_val, nb_couleurs):
    # On ajoute taille_totale en global pour pouvoir la modifier selon le CSV
    global taille_totale, banque, couleur_dis, delay, score

    niveau2 = diff_val == "2"
    user_choice = int(mode_val)

    if user_choice == 1:  # MODE IMPORTATION
        fichier_nom = "exemple_grille.csv"
        dossier_actuel = os.path.dirname(os.path.abspath(__file__))
        chemin_complet = os.path.join(dossier_actuel, fichier_nom)

        if os.path.exists(chemin_complet):
            # 1. Extraction et conversion forcée en entiers
            modele_brut = extraire_csv(chemin_complet, True)
            modele_raw = [[int(case) for case in ligne] for ligne in modele_brut]

            # 2. Mise à jour dynamique de la TAILLE
            taille_totale = len(modele_raw)

            # 3. Calcul dynamique des COULEURS présentes
            max_index = 0
            for ligne in modele_raw:
                if ligne:  # Sécurité ligne vide
                    max_index = max(max_index, max(ligne))

            couleurs = banque[: max_index + 1] + [couleur_dis]

        else:
            print(f"Erreur : Posez un fichier nommé '{fichier_nom}' à côté du script.")
            return

    else:  # MODE ALÉATOIRE
        n_couleurs = int(nb_couleurs)
        # On utilise la taille_totale par défaut (7)
        couleurs = banque[:n_couleurs] + [couleur_dis]

        modele_raw = creer_monde_random(n_couleurs, taille_totale)
        while (test_alignement(modele_raw, niveau2) != []) or (
            not prevision(modele_raw, niveau2)
        ):
            modele_raw = creer_monde_random(n_couleurs, taille_totale)

    # Lancement avec les variables mises à jour
    start_affichage(taille_totale, couleurs, modele_raw, delay, niveau2, score)
