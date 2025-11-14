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
    N = 5
    M = 6
    P = 17
    grille_poids = genere_poids(N,M)
    
    affiche_matrice(grille_poids,N,M)
    contraintes,secondmb = resolution_grille(P,N,M)
    #affichage_contrainte(contraintes,secondmb,N,M)
    f_obj = fonction_objectif(grille_poids,N,M)
    sol = solution_grille(contraintes,secondmb,f_obj,N,M)
    grille = vecteur_to_matrice(sol,N,M)
    affiche_matrice(grille,N,M)
    
    