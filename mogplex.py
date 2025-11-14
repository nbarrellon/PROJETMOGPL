#!/usr/bin/python

# Copyright 2025, Gurobi Optimization, Inc.

from gurobipy import *
from testgurobi import *
from dessin import *

def solution_grille(contraintes:list[list[int]],scdmb:list[int],fonction_obj:list[int],N:int,M:int)->list[int]:
    """
    Renvoie la solution du PL
    Entrée : contraintes du PL (coefficient et second membre), fonction objectif, taille de la matrice 
    Sortie : Liste de taille N*M avec la valeur des variables de décision (0 ou 1)
    """
    nbcont=len(contraintes) #Ncontraintes sur les lignes, M contraintes sur les colonnes 
    nbvar=N*M #il y a autant de variable que de cases
    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)
    m = Model("mogplex")       
    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.BINARY, lb=0, name="x%d" % (i+1)))
    # maj du modele pour integrer les nouvelles variables
    m.update()
    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += fonction_obj[j] * x[j]    
    # definition de l'objectif
    m.setObjective(obj,GRB.MINIMIZE)
    # Definition des contraintes
    for i in lignes:
        m.addConstr(quicksum(contraintes[i][j]*x[j] for j in colonnes) <= scdmb[i], "Contrainte%d" % i)
    # Resolution
    m.optimize()
    solution = []
    for j in colonnes:
        solution.append(int(x[j].x))
    return solution

def vecteur_to_matrice(v,N,M):
    """
    Reçoit la solution donnée par Gurobi sous forme de vecteur de taille N*M
    Renvoie la grille correspondante : matrice de N par M
    """
    grille = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(len(v)):
        grille[i//M][i%M]=v[i]
    return grille

if __name__=="__main__":
    N = 11
    M = 11
    P = 62
    grille_poids = genere_poids(N,M)
    #grille_poids = [[351, 406, 253, 216, 622, 5, 348, 769, 438, 771], [347, 879, 538, 191, 722, 492, 495, 575, 206, 938], [138, 983, 346, 621, 546, 947, 806, 248, 26, 346], [733, 938, 186, 588, 824, 263, 960, 980, 560, 284], [437, 646, 905, 164, 275, 123, 922, 5, 80, 270], [225, 555, 533, 480, 498, 639, 352, 906, 488, 235], [9, 142, 507, 270, 806, 319, 562, 870, 942, 386], [626, 262, 675, 470, 823, 825, 427, 682, 457, 924], [981, 596, 18, 220, 34, 33, 933, 726, 325, 480], [420, 56, 391, 807, 321, 606, 976, 984, 202, 816]]
    #print(grille_poids)
    affiche_matrice(grille_poids,N,M)
    contraintes,secondmb = resolution_grille(P,N,M)
    #affichage_contrainte(contraintes,secondmb,N,M)
    f_obj = fonction_objectif(grille_poids,N,M)
    sol = solution_grille(contraintes,secondmb,f_obj,N,M)
    grille = vecteur_to_matrice(sol,N,M)
    affiche_matrice(grille,N,M)
    
    