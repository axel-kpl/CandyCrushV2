def test_alignement(grille):
    """
    renvoie les coordonnées (liste de tuples (x, y)) des groupe de pions dont au moins trois sont alignés et de même couleur
    complexité : O(n²)
    """
    res = []
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            nb = grille[i][j]
            if (
                not (i <= 0 or i >= len(grille) - 1)
                and grille[i - 1][j] == nb
                and grille[i + 1][j] == nb
            ):
                if not (i - 1, j) in res:
                    res.append((i - 1, j))
                if not (i, j) in res:
                    res.append((i, j))
                if not (i + 1, j) in res:
                    res.append((i + 1, j))
            if (
                not (j <= 0 or j >= len(grille[0]) - 1)
                and grille[i][j - 1] == nb
                and grille[i][j + 1] == nb
            ):
                if not (i, j - 1) in res:
                    res.append((i, j - 1))
                if not (i, j) in res:
                    res.append((i, j))
                if not (i, j + 1) in res:
                    res.append((i, j + 1))
    new = pions_autour(grille, res)
    while new != []:
        for x, y in new:
            res.append((x, y))
            new = pions_autour(grille, res)
    return res


def pions_autour(grille, res):
    """
    renvoie tout les pions adjacent et de la même couleur que les pions du groupe res
    complexité : O(n)
    """
    new = []
    for i, j in res:
        nb = grille[i][j]
        if (
            not i <= 0
            and grille[i - 1][j] == nb
            and not (i - 1, j) in res
            and not (i - 1, j) in new
        ):
            new.append((i - 1, j))
        if (
            not j <= 0
            and grille[i][j - 1] == nb
            and not (i, j - 1) in res
            and not (i, j - 1) in new
        ):
            new.append((i, j - 1))
        if (
            not i >= len(grille) - 1
            and grille[i + 1][j] == nb
            and not (i + 1, j) in res
            and not (i + 1, j) in new
        ):
            new.append((i + 1, j))
        if (
            not j >= len(grille[0]) - 1
            and grille[i][j + 1] == nb
            and not (i, j + 1) in res
            and not (i, j + 1) in new
        ):
            new.append((i, j + 1))
    return new
