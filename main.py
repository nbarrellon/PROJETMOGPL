from Graphe import *
from generation_instance import *

def lecture_fichier_instance(fichier):
    with open(fichier,"r",encoding='utf-8') as f:
        ligne1 = f.readline().split()
        N = int(ligne1[0])
        M = int(ligne1[1])
        grille = []
        for i in range(N):
            ligne = f.readline().split()
            grille.append([int(x) for x in ligne])
        derniere_ligne = f.readline().split()
        D1 = int(derniere_ligne[0])
        D2 = int(derniere_ligne[1])
        F1 = int(derniere_ligne[2])
        F2 = int(derniere_ligne[3])
        orientation = derniere_ligne[4]
        f.readline() #on saute les 0 0 de la fin
    return grille,D1,D2,F1,F2,orientation

grille,D1,D2,F1,F2,orientation = lecture_fichier_instance("essai2.txt")
g = Graphe(grille)