import tkinter as tk
import time

#Cette fonction a été entièrement réalisée à ma demande
# et sous ma direction par l'IA. (Le Chat, une assistante IA développée par Mistral AI.)

def dessiner_grille(grille, points, chemin, chemin_texte, orientation_depart, grille_pondération=None):
    taille_case = 30
    marge = 20
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    fenetre = tk.Tk()
    fenetre.title("La balade du robot")

    # Canevas pour la grille
    canevas = tk.Canvas(fenetre, width=nb_colonnes*taille_case + 2*marge, height=nb_lignes*taille_case + 2*marge, bg='white')
    canevas.pack()

    # Dessiner la grille avec une marge
    for i in range(nb_lignes + 1):
        canevas.create_line(marge, marge + i*taille_case, marge + nb_colonnes*taille_case, marge + i*taille_case, fill='black')
    for j in range(nb_colonnes + 1):
        canevas.create_line(marge + j*taille_case, marge, marge + j*taille_case, marge + nb_lignes*taille_case, fill='black')

    # Dessiner les cases bleues avec une marge et un léger retrait
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if grille[i][j] == 1:
                retrait = 2
                canevas.create_rectangle(
                    marge + j*taille_case + retrait, marge + i*taille_case + retrait,
                    marge + (j+1)*taille_case - retrait, marge + (i+1)*taille_case - retrait,
                    fill='lightblue', outline=''
                )

    # Dessiner les coefficients si grille_pondération est fournie
    if grille_pondération is not None:
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                
                canevas.create_text(
                        marge + j*taille_case + taille_case//2,
                        marge + i*taille_case + taille_case//2,
                        text=str(grille_pondération[i][j]), fill='black', font=('Arial', 8)
                    )

    # Dessiner les points noirs aux intersections avec une marge
    for point in points:
        y, x = point
        canevas.create_oval(
            marge + x*taille_case-5, marge + y*taille_case-5,
            marge + x*taille_case+5, marge + y*taille_case+5, fill='black'
        )

    # Dessiner le chemin rouge reliant les intersections avec une marge
    if chemin:
        for k in range(len(chemin) - 1):
            y1, x1 = chemin[k]
            y2, x2 = chemin[k+1]
            canevas.create_line(
                marge + x1*taille_case, marge + y1*taille_case,
                marge + x2*taille_case, marge + y2*taille_case, fill='red', width=2
            )

    # Dessiner la flèche d'orientation du point de départ
    if chemin:
        y, x = chemin[0]
        if orientation_depart == "nord":
            canevas.create_line(marge + x*taille_case, marge + y*taille_case - 10,
                                marge + x*taille_case, marge + y*taille_case - 20, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "sud":
            canevas.create_line(marge + x*taille_case, marge + y*taille_case + 10,
                                marge + x*taille_case, marge + y*taille_case + 20, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "est":
            canevas.create_line(marge + x*taille_case + 10, marge + y*taille_case,
                                marge + x*taille_case + 20, marge + y*taille_case, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "ouest":
            canevas.create_line(marge + x*taille_case - 10, marge + y*taille_case,
                                marge + x*taille_case - 20, marge + y*taille_case, fill='black', arrow=tk.LAST, width=2)

    # Afficher le chemin sous forme de chaîne de caractères
    label_chemin = tk.Label(fenetre, text=chemin_texte, font=('Arial', 12), bg='white')
    label_chemin.pack()

    fenetre.mainloop()

import tkinter as tk
import time

def dessiner_grille_2(grille, points, chemin, chemin_texte, orientation_depart, grille_pondération=None):
    taille_case = 30
    marge = 20
    nb_lignes = len(grille)
    nb_colonnes = len(grille[0])

    fenetre = tk.Tk()
    fenetre.title("La balade du robot")

    # Canevas pour la grille
    canevas = tk.Canvas(fenetre, width=nb_colonnes*taille_case + 2*marge, height=nb_lignes*taille_case + 2*marge, bg='white')
    canevas.pack()

    # Dessiner la grille avec une marge
    for i in range(nb_lignes + 1):
        canevas.create_line(marge, marge + i*taille_case, marge + nb_colonnes*taille_case, marge + i*taille_case, fill='black')
    for j in range(nb_colonnes + 1):
        canevas.create_line(marge + j*taille_case, marge, marge + j*taille_case, marge + nb_lignes*taille_case, fill='black')

    # Dessiner les cases bleues avec une marge et un léger retrait
    for i in range(nb_lignes):
        for j in range(nb_colonnes):
            if grille[i][j] == 1:
                retrait = 2
                canevas.create_rectangle(
                    marge + j*taille_case + retrait, marge + i*taille_case + retrait,
                    marge + (j+1)*taille_case - retrait, marge + (i+1)*taille_case - retrait,
                    fill='lightblue', outline=''
                )

    # Dessiner les coefficients si grille_pondération est fournie
    if grille_pondération is not None:
        for i in range(nb_lignes):
            for j in range(nb_colonnes):
                if grille_pondération[i][j] is not None:
                    canevas.create_text(
                        marge + j*taille_case + taille_case//2,
                        marge + i*taille_case + taille_case//2,
                        text=str(grille_pondération[i][j]), fill='black', font=('Arial', 8)
                    )

    # Dessiner les points noirs aux intersections avec une marge
    for point in points:
        y, x = point
        canevas.create_oval(
            marge + x*taille_case-5, marge + y*taille_case-5,
            marge + x*taille_case+5, marge + y*taille_case+5, fill='black'
        )

    # Dessiner la flèche d'orientation du point de départ
    if chemin:
        y, x = chemin[0]
        if orientation_depart == "nord":
            canevas.create_line(marge + x*taille_case, marge + y*taille_case - 10,
                                marge + x*taille_case, marge + y*taille_case - 20, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "sud":
            canevas.create_line(marge + x*taille_case, marge + y*taille_case + 10,
                                marge + x*taille_case, marge + y*taille_case + 20, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "est":
            canevas.create_line(marge + x*taille_case + 10, marge + y*taille_case,
                                marge + x*taille_case + 20, marge + y*taille_case, fill='black', arrow=tk.LAST, width=2)
        elif orientation_depart == "ouest":
            canevas.create_line(marge + x*taille_case - 10, marge + y*taille_case,
                                marge + x*taille_case - 20, marge + y*taille_case, fill='black', arrow=tk.LAST, width=2)

    # Animation du chemin
    if chemin:
        for k in range(len(chemin) - 1):
            y1, x1 = chemin[k]
            y2, x2 = chemin[k+1]
            # Dessiner le segment du chemin
            canevas.create_line(
                marge + x1*taille_case, marge + y1*taille_case,
                marge + x2*taille_case, marge + y2*taille_case, fill='red', width=2
            )
            # Mettre à jour le canevas
            fenetre.update()
            # Attendre un court instant pour l'animation
            time.sleep(1)

    # Afficher le chemin sous forme de chaîne de caractères
    label_chemin = tk.Label(fenetre, text=chemin_texte, font=('Arial', 12), bg='white')
    label_chemin.pack()

    fenetre.mainloop()

