import matplotlib.pyplot as plt
from matplotlib.widgets import Button, RadioButtons, Slider
import main_mat

# Liste pour stocker [Difficulté, Mode, Nb_Couleurs]
# Difficulté "1", Mode "2" (Aléatoire), Couleurs 5
reglages = ["1", "2", 5]


def maj_diff(label):
    reglages[0] = "1" if label == "Normal" else "2"


def maj_mode(label):
    reglages[1] = "1" if label == "Importer (exemple_grille.csv)" else "2"


def maj_slider(val):
    reglages[2] = int(val)


def lancer(event):
    plt.close()  # Ferme le menu
    main_mat.lancer_partie(reglages[0], reglages[1], reglages[2])


# Création de la figure
fig, ax = plt.subplots(figsize=(8, 7))
plt.subplots_adjust(left=0.1, bottom=0.1, top=0.9)
ax.axis("off")

# titre
fig.patch.set_facecolor("#F7F7F7")
ax.text(
    0.5,
    0.95,
    "Candy Crush - ISN",
    fontsize=18,
    fontweight="bold",
    ha="center",
    color="#AE00B0",
)

# --- SECTION RÉGLAGES (Le "Sous-Menu" visuel) ---
ax.text(0.5, 0.85, "Lancer le jeu", fontsize=12, ha="center", color="gray")

# 1. Choix de la difficulté
ax.text(0.1, 0.75, "Difficulté :", fontsize=10, fontweight="bold")
ax_diff = plt.axes([0.1, 0.68, 0.35, 0.06], facecolor="#EEEEEE")
radio_diff = RadioButtons(ax_diff, ("Niveau 1", "Niveau 2 (Voir Moodle)"))
radio_diff.on_clicked(maj_diff)

# 2. import du CSV ou aléatoire
ax_mode = plt.axes([0.55, 0.68, 0.35, 0.06], facecolor="#EEEEEE")
radio_mode = RadioButtons(ax_mode, ("Aléatoire", "Importer (exemple_grille.csv)"))
radio_mode.on_clicked(maj_mode)

# 3. slide pour le nombre de couleurs
ax.text(
    0.5,
    0.55,
    "Nombre de couleurs (3 à 7) :",
    fontsize=10,
    fontweight="bold",
    ha="center",
)
ax_slider = plt.axes([0.2, 0.48, 0.6, 0.03], facecolor="#FFD1FB")
slider_c = Slider(ax_slider, "", 3, 7, valinit=5, valstep=1, color="#AE00B0")
slider_c.on_changed(maj_slider)

# appel aux fonctions + boutons jouer
ax_btn = plt.axes([0.3, 0.15, 0.4, 0.12])
btn_jouer = Button(ax_btn, "Jouer", color="#96FFB5", hovercolor="#498100")
btn_jouer.label.set_fontsize(12)
btn_jouer.label.set_fontweight("bold")
btn_jouer.on_clicked(lancer)

plt.show()
