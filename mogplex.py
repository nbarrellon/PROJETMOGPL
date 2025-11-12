#!/usr/bin/python

# Copyright 2025, Gurobi Optimization, Inc.

from gurobipy import *
from testgurobi import *

def solution_grille(contraintes,scdmb,fonction_obj,N,M):
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
    print("")                
    print('Solution optimale:')
    for j in colonnes:
        print('x%d'%(j+1), '=', x[j].x)
    print("")
    print('Valeur de la fonction objectif :', m.objVal)

N = 5
M = 5
P = 5  
grille_poids = genere_poids(N,M)
affiche_matrice(grille_poids,N,M)
contraintes,secondmb = resolution_grille(P,N,M)
f_obj = fonction_objectif(grille_poids,N,M)
solution_grille(contraintes,secondmb,f_obj,N,M)