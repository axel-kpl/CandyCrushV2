from random import randint
from tkinter import *


#      __                .__              ____
#    _/  |______    ____ |  |__   ____   /_   |
#    \   __\__  \ _/ ___\|  |  \_/ __ \   |   |
#     |  |  / __ \\  \___|   Y  \  ___/   |   |
#     |__| (____  /\___  >___|  /\___  >  |___|
#               \/     \/     \/     \/


def extraire_csv(nom_fichier: str, type_int=True) -> list:
    """Extrait un fichier csv d'une partie de CandyCrush et renvoie une liste 2D
    de chiffre de type int !!"""
    grille = []
    with open(nom_fichier, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            current = []
            for element in ligne:
                if (
                    element != " " and element != "\n"
                ):  # on ignore les espaces et les retours à la ligne
                    if type_int:
                        current.append(int(element))
                    else:
                        current.append(element)
            grille.append(current)
    return grille


liste = extraire_csv("exemple_grille.csv")
print(liste)


def creer_monde_random(nbr_type_bonbons: int, taille_liste: int) -> list:
    """Crée une liste 2D composée de valeurs aléatoires allant de 0 à nbr_max-1
    correspondant aux couleurs des bonbons"""
    grille = []
    for _ in range(taille_liste):
        ligne = [0] * taille_liste
        for i in range(len(ligne)):
            ligne[i] = randint(0, nbr_type_bonbons - 1)
        grille.append(ligne)
    return grille


#      __                .__             ________
#    _/  |______    ____ |  |__   ____   \_____  \
#    \   __\__  \ _/ ___\|  |  \_/ __ \    _(__  <
#     |  |  / __ \\  \___|   Y  \  ___/   /       \
#     |__| (____  /\___  >___|  /\___  > /______  /
#               \/     \/     \/     \/         \/


def test_alignement(grille: list):
    res = set()  # On utilise un set pour éviter les doublons
    hauteur = len(grille)
    largeur = len(grille[0])

    for i in range(hauteur):
        for j in range(largeur):
            couleur_actuelle = grille[i][j]
            if couleur_actuelle == -1:
                continue  # gestion de cases vides

            # --- Vérification Horizontale (3 à la suite) ---
            if j < largeur - 2:  # On s'arrête à 2 cases du bord droit
                if (
                    grille[i][j + 1] == couleur_actuelle
                    and grille[i][j + 2] == couleur_actuelle
                ):
                    res.add((i, j))
                    res.add((i, j + 1))
                    res.add((i, j + 2))

            # --- Vérification Verticale (3 à la suite) ---
            if i < hauteur - 2:  # On s'arrête à 2 cases du bas
                if (
                    grille[i + 1][j] == couleur_actuelle
                    and grille[i + 2][j] == couleur_actuelle
                ):
                    res.add((i, j))
                    res.add((i + 1, j))
                    res.add((i + 2, j))

    #  on converti l'ensemble en liste pour renvoyer
    return list(res)


def pions_autour(grille: list, res: tuple):
    """
    renvoie tout les pions adjacent et de la même couleur que les pions du groupe res
    """
    new = []
    for i, j in res:
        nb = grille[i][j]
        if (
            not i == 0
            and grille[i - 1][j] == nb
            and not (i - 1, j) in res
            and not (i - 1, j) in new
        ):
            new.append((i - 1, j))
        if (
            not j == 0
            and grille[i][j - 1] == nb
            and not (i, j - 1) in res
            and not (i, j - 1) in new
        ):
            new.append((i, j - 1))
        if (
            not i == len(grille) - 1
            and grille[i + 1][j] == nb
            and not (i + 1, j) in res
            and not (i + 1, j) in new
        ):
            new.append((i + 1, j))
        if (
            not j == len(grille[0]) - 1
            and grille[i][j + 1] == nb
            and not (i, j + 1) in res
            and not (i, j + 1) in new
        ):
            new.append((i, j + 1))
    return new


#      __                .__                _____
#    _/  |______    ____ |  |__   ____     /  |  |
#    \   __\__  \ _/ ___\|  |  \_/ __ \   /   |  |_
#     |  |  / __ \\  \___|   Y  \  ___/  /    ^   /
#     |__| (____  /\___  >___|  /\___  > \____   |
#               \/     \/     \/     \/       |__|


def modifier_grille(grille, coordonnees):
    """
    Remplace tous les bonbons présents aux coordonnées entrées par les bonbons présents
    sur les cases juste au dessus. (Tant que la ligne au dessus contient des bonbons,
    remplacer les bonbons par ceux de la ligne juste au dessus, et si la ligne au dessus ne
    contient pas de bonbons c’est que on est en haut de la grille et il faut remplacer les cases
    vides par des bonbons aléatoires), fait tomber les bonbons sur les cases vides
    verticalement et complète les cases du haut par des bonbons aléatoires.
    """
    for i in range(len(coordonnees)):
        indice_ligne = coordonnees[i][0]
        indice_colonne = coordonnees[i][1]
        while (
            indice_ligne != 0
        ):  # On évite de faire appel à une ligne au dessus de la ligne la plus haute de la grille.
            grille[indice_ligne][indice_colonne] = grille[indice_ligne - 1][
                indice_colonne
            ]
            indice_ligne = indice_ligne - 1
        # On remplace les bonbons de la ligne tout en haut par un bonbon aléatoire.
        # Pour simplifier le code on évite de créer un alignement dans la partie non visible de la grille.

        grille[indice_ligne][indice_colonne] = random.randint(0, 3)
        if (
            indice_colonne != 0 and indice_colonne != len(grille[0]) - 1
        ):  # On évite de travailler sur des colonnes inexistantes.
            while (
                grille[indice_ligne][indice_colonne]
                == grille[indice_ligne][indice_colonne - 1]
                or grille[indice_ligne][indice_colonne]
                == grille[indice_ligne][indice_colonne + 1]
                or grille[indice_ligne + 1][indice_colonne]
                == grille[indice_ligne][indice_colonne]
            ):
                grille[indice_ligne][indice_colonne] = random.randint(0, 3)
        else:
            while (
                grille[indice_ligne][indice_colonne]
                == grille[indice_ligne + 1][indice_colonne]
            ):
                grille[indice_ligne][indice_colonne] = random.randint(0, 3)


#      __                .__              .________
#    _/  |______    ____ |  |__   ____    |   ____/
#    \   __\__  \ _/ ___\|  |  \_/ __ \   |____  \
#     |  |  / __ \\  \___|   Y  \  ___/   /       \
#     |__| (____  /\___  >___|  /\___  > /______  /
#               \/     \/     \/     \/         \/


def prevision(grille):
    """
    Renvoie True si un coup est possible sur cette grille, False sinon
    """
    grille_bis = [
        [grille[a][b] for b in range(len(grille[0]))] for a in range(len(grille))
    ]
    test = False
    i = 0
    j = 0
    while not test and i < len(grille) and j < len(grille[0]):
        if not i == 0:
            grille_bis[i - 1][j], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i - 1][j],
            )
            if test_alignement(grille_bis) != []:
                test = True
            grille_bis[i - 1][j], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i - 1][j],
            )
        if not j == 0:
            grille_bis[i][j - 1], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i][j - 1],
            )
            if test_alignement(grille_bis) != []:
                test = True
            grille_bis[i][j - 1], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i][j - 1],
            )
        if not i == len(grille) - 1:
            grille_bis[i + 1][j], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i + 1][j],
            )
            if test_alignement(grille_bis) != []:
                test = True
            grille_bis[i + 1][j], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i + 1][j],
            )
        if not j == len(grille[0]) - 1:
            grille_bis[i][j + 1], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i][j + 1],
            )
            if test_alignement(grille_bis) != []:
                test = True
            grille_bis[i][j + 1], grille_bis[i][j] = (
                grille_bis[i][j],
                grille_bis[i][j + 1],
            )
        i += 1
        j += 1
    return test


#      __                .__               ________
#    _/  |______    ____ |  |__   ____    /  _____/
#    \   __\__  \ _/ ___\|  |  \_/ __ \  /   __  \
#     |  |  / __ \\  \___|   Y  \  ___/  \  |__\  \
#     |__| (____  /\___  >___|  /\___  >  \_____  /
#               \/     \/     \/     \/         \/


def coup(grille: list, r1: int, c1: int, r2: int, c2: int) -> bool:
    """
    Echange deux bonbons. Si un alignement est créé, l'échange reste et la fonction renvoie True.
    Sinon, on annule et renvoie False.
    """
    # on swap les deux bonbons de la grille
    grille[r1][c1], grille[r2][c2] = grille[r2][c2], grille[r1][c1]

    # on récupère la liste des alignements (tous les alignements de la grille)
    alignements = test_alignement(grille)

    # si la liste n'est pas vide, c'est que le coup est faisable
    if alignements != []:
        return True
    else:
        # sinon pas de combinaison possible donc on annule le swap
        grille[r1][c1], grille[r2][c2] = grille[r2][c2], grille[r1][c1]
        return False


#      __                .__             ________
#    _/  |______    ____ |  |__   ____   \_____  \
#    \   __\__  \ _/ ___\|  |  \_/ __ \   /  ____/
#     |  |  / __ \\  \___|   Y  \  ___/  /       \
#     |__| (____  /\___  >___|  /\___  > \_______ \
#               \/     \/     \/     \/          \/


def rafraichir_interface():
    """Met à jour les couleurs des bonbons sur la grille (swap)"""
    for i in range(taille_totale):
        for j in range(taille_totale):
            labels_grille[i][j].config(
                bg=couleurs[modele_raw[i][j]], relief="ridge", borderwidth=2
            )


def gerer_clic(r, c):
    global premier_clic

    # 1. Premier clic : On sélectionne la case
    if premier_clic is None:
        premier_clic = (r, c)
        labels_grille[r][c].config(
            highlightbackground="black"
        )  # selectionne la case en noir

    else:
        r1, c1 = premier_clic
        r2, c2 = r, c

        # On vérifie si c'est la MÊME case (pour désélectionner)
        if (r1, c1) == (r2, c2):
            premier_clic = None
            rafraichir_interface()
            return

        # on calcule une distance algebrique entre deux cases
        dist = abs(r1 - r2) + abs(c1 - c2)

        # si elle sont a proximité (dist =1)
        if dist == 1:

            print(f"Échange réussi entre [{r1},{c1}] et [{r2},{c2}]")
        else:
            print("Coup invalide ou trop loin")

        # on reset a aucun clic, et on rafriachit l'interface pour enlever les bordures
        premier_clic = None
        rafraichir_interface()


def start_affichage(taille_totale, couleurs, modele_raw, labels_grille):
    """lance l'affichage de la fenetre tk"""
    root = Tk()
    root.title("Candy Crush • ISN")

    # Configuration du redimensionnement
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)
    root.geometry("500x500")  # Largeur x Hauteur : on fait un carré pour le lancemennt

    frm = ttk.Frame(root, padding=50)
    frm.grid(sticky="nsew")

    for i in range(taille_totale):
        frm.rowconfigure(i, weight=1)
        frm.columnconfigure(i, weight=1)
        for j in range(taille_totale):
            # On crée un Label standard (tk.Label) car ttk.Label est plus limité pour les couleurs directes

            lbl = Label(
                frm,
                text=f"",
                bg=couleurs[modele_raw[i][j]],
                fg="white",
                relief="flat",
                padx=0,
                pady=0,
                highlightthickness=3,  # permet de gerer le la selection d'une case qui fait depasser la bordure {cadre noir}
                highlightbackground="#F0F0F0",
            )
            # On lie l'événement clic (lambda est nécessaire pour passer les coordonnées)
            lbl.bind("<Button-1>", lambda event, r=i, c=j: gerer_clic(r, c))

            # On stocke le widget pour pouvoir le modifier plus tard
            labels_grille[i][j] = lbl

            lbl.grid(column=j, row=i, sticky="nsew", padx=3, pady=3)
    rafraichir_interface()

    root.mainloop()
