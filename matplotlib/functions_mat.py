from random import randint
from matplotlib import patches
from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt

#      __                .__              ____
#    _/  |______    ____ |  |__   ____   /_   |
#    \   __\__  \ _/ ___\|  |  \_/ __ \   |   |
#     |  |  / __ \\  \___|   Y  \  ___/   |   |
#     |__| (____  /\___  >___|  /\___  >  |___|
#               \/     \/     \/     \/


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
            if couleur_actuelle == 5:
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
def modifier_grille(grille, coordonnees, nbr_pions=5):
    if not coordonnees:
        return

    largeur = len(grille[0])
    hauteur = len(grille)
    # On utilise un set pour être sûr de ne pas traiter deux fois la même case
    coords_uniques = set(coordonnees)

    for j in range(largeur):
        # On extrait les lignes concernées pour la colonne j, du bas vers le haut
        colonne_restante = []
        for i in range(hauteur):
            if (i, j) not in coords_uniques:
                colonne_restante.append(grille[i][j])

        nb_nouveaux = hauteur - len(colonne_restante)

        nouveaux_bonbons = [randint(0, nbr_pions - 1) for _ in range(nb_nouveaux)]

        nouvelle_colonne = nouveaux_bonbons + colonne_restante

        for i in range(hauteur):
            grille[i][j] = nouvelle_colonne[i]


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
        i = i + 1
        if i == len(grille):
            i = 0
            j = j + 1
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
    if len(alignements) > 0:
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


def rafraichir_interface(modele_raw, image_objet, fig):
    """Met à jour les couleurs des bonbons sur la grille (swap)"""
    image_objet.set_data(modele_raw)
    fig.canvas.draw_idle()  # Redessine la figure


def gerer_clic(
    taille_totale, event, img, ax, fig, premier_clic, modele_raw, couleurs, delay
):

    # 1er clic
    if premier_clic[0] is None:
        if event.xdata is None or event.ydata is None:
            return  # gestion clic dehors grille
        c = int(round(event.xdata))
        r = int(round(event.ydata))
        premier_clic[0] = (r, c)
        rect = patches.Rectangle(
            (c - 0.5, r - 0.5), 1, 1, linewidth=3, edgecolor="#96FFB5", fill=False
        )
        ax.add_patch(rect)
        fig.canvas.draw_idle()
    # sinon c'est le deuxieme clic
    else:
        if event.xdata is None or event.ydata is None:
            return  # gestion clic dehors grille
        c = int(round(event.xdata))
        r = int(round(event.ydata))
        r1, c1 = premier_clic[0]
        r2, c2 = r, c

        # on enleve le carree de surbrillance
        for patch in ax.patches[::-1]:
            patch.remove()
        premier_clic[0] = None

        # On vérifie si c'est la MÊME case (pour désélectionner)
        if (r1, c1) == (r2, c2):
            rafraichir_interface(modele_raw, img, fig)
            return

        # on calcule une distance algebrique entre deux cases
        lat = abs(r1 - r2)
        lon = abs(c1 - c2)
        # si elle sont a proximité (dist =1)
        if (lat + lon) == 1 and coup(modele_raw, r1, c1, r2, c2):
            print(f"Échange réussi entre [{r1},{c1}] et [{r2},{c2}]")
            rafraichir_interface(modele_raw, img, fig)
            plt.pause(delay)
            fini = test_alignement(modele_raw)
            while len(fini) > 0:
                for r, c in fini:
                    modele_raw[r][c] = len(couleurs) - 1
                rafraichir_interface(modele_raw, img, fig)
                plt.pause(delay)

                modifier_grille(modele_raw, fini)
                rafraichir_interface(modele_raw, img, fig)
                plt.pause(delay)
                fini = test_alignement(modele_raw)
        else:
            print("Coup invalide ou trop loin")

        rafraichir_interface(modele_raw, img, fig)


def start_affichage(taille_totale, couleurs, modele_raw, delay):
    """lance l'affichage de la fenetre matplotlib"""

    hauteur = len(modele_raw)
    largeur = len(modele_raw[0])

    fig, ax = plt.subplots()

    cmap_custom = ListedColormap(couleurs)

    img = ax.imshow(
        modele_raw,
        cmap=cmap_custom,
        vmin=0,
        vmax=len(couleurs) - 1,
        extent=[-0.5, largeur - 0.5, hauteur - 0.5, -0.5],
    )
    # ajout des grilles noires pour plus de visibilité

    ax.set_xticks([x + 0.5 for x in range(largeur - 1)])
    ax.set_yticks([x + 0.5 for x in range(hauteur - 1)])
    ax.grid(True, color="#000000", linestyle="-", linewidth=1)
    ax.set_axisbelow(False)
    ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)

    selection_rect = [None]

    cid = fig.canvas.mpl_connect(
        "button_press_event",
        lambda event: gerer_clic(
            taille_totale,
            event,
            img,
            ax,
            fig,
            selection_rect,
            modele_raw,
            couleurs,
            delay,
        ),
    )

    plt.show()


#
#      ____   _________  __
#    _/ ___\ /  ___/\  \/ /
#    \  \___ \___ \  \   /
#     \___  >____  >  \_/
#         \/     \/


def extraire_csv(nom_fichier: str, type_int=True) -> list:
    """Extrait un fichier csv d'une partie de CandyCrush et renvoie une liste 2D
    de chiffre de type int !! si type_int est set a True"""
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
    if not (test_alignement(grille) != []) or (not prevision(grille)):
        return grille
    raise (
        ValueError(
            "La grille ne possède pas de coup jouable au prochain tour / admet deja des coups"
        )
    )
