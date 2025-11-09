import tkinter as tk

def dessiner_grille_intersections(grille, points, chemin):
    taille_case = 50
    marge = 20
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    fenetre = tk.Tk()
    fenetre.title("Grille avec Chemin aux Intersections")

    # Canevas pour la grille
    canevas = tk.Canvas(fenetre, width=nb_colonnes*taille_case + 2*marge, height=nb_lignes*taille_case + 2*marge, bg='white')
    canevas.pack()

    # Dessiner la grille avec une marge
    for i in range(nb_lignes + 1):
        canevas.create_line(marge, marge + i*taille_case, marge + nb_colonnes*taille_case, marge + i*taille_case, fill='black')
    for j in range(nb_colonnes + 1):
        canevas.create_line(marge + j*taille_case, marge, marge + j*taille_case, marge + nb_lignes*taille_case, fill='black')

    # Dessiner les cases bleues avec une marge
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if grille[i][j] == 1:
                canevas.create_rectangle(marge + j*taille_case, marge + i*taille_case,
                                         marge + (j+1)*taille_case, marge + (i+1)*taille_case,
                                         fill='lightblue', outline='')

    # Dessiner les points noirs aux intersections avec une marge
    for point in points:
        x, y = point
        canevas.create_oval(marge + x*taille_case-5, marge + y*taille_case-5,
                            marge + x*taille_case+5, marge + y*taille_case+5, fill='black')

    # Dessiner le chemin rouge reliant les intersections avec une marge
    if chemin:
        for k in range(len(chemin) - 1):
            x1, y1 = chemin[k]
            x2, y2 = chemin[k+1]
            canevas.create_line(marge + x1*taille_case, marge + y1*taille_case,
                                marge + x2*taille_case, marge + y2*taille_case, fill='red', width=2)

    # Afficher le chemin sous forme de chaîne de caractères
    chemin_texte = " → ".join(f"({x}, {y})" for x, y in chemin)
    label_chemin = tk.Label(fenetre, text=chemin_texte, font=('Arial', 12), bg='white')
    label_chemin.pack()

    fenetre.mainloop()

# Exemple d'utilisation
grille = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Mise à jour de la grille avec les cases bleues (1)
grille[1][1] = 1
grille[2][3] = 1
grille[3][4] = 1
grille[4][2] = 1
grille[5][5] = 1
grille[6][7] = 1
grille[7][0] = 1

points = [(1, 1), (6, 6)]  # Coordonnées des intersections
chemin = [(1, 1), (1, 2), (2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (5, 4), (5, 5), (6, 5), (6, 6)]  # Coordonnées des intersections

dessiner_grille_intersections(grille, points, chemin)
