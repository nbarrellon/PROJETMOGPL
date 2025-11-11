#!/usr/bin/python

# Copyright 2025, Gurobi Optimization, Inc.


from gurobipy import *

def resolution_grille(grille,N,M):
    nbcont=N+M #Ncontraintes sur les lignes, M contraintes sur les colonnes 
    nbvar=N*M #il y a autant de variable que de cases

    # Range of plants and warehouses
    lignes = range(nbcont)
    colonnes = range(nbvar)

    # Matrice des contraintes a = grille avec les poids
    a = [g for g in grille] #contraintes sur les lignes
    for j in range(M):
        colonne = []
        for i in range(N):
            colonne.append(grille[i][j])
        a.append(colonne) #contrainte sur les colonnes

# Second membre
    b = [2*P/M for _ in range(M)] #seconde membre contraintes lignes
    b += [2*P/N for _ in range(N)] #second membre contraintes colonnes

    # Coefficients de la fonction objectif
    c = [4, 10]

    m = Model("mogplex")     
            
    # declaration variables de decision
    x = []
    for i in colonnes:
        x.append(m.addVar(vtype=GRB.CONTINUOUS, lb=0, name="x%d" % (i+1)))

    # maj du modele pour integrer les nouvelles variables
    m.update()

    obj = LinExpr();
    obj =0
    for j in colonnes:
        obj += c[j] * x[j]
            
    # definition de l'objectif
    m.setObjective(obj,GRB.MAXIMIZE)

    # Definition des contraintes
    for i in lignes:
        m.addConstr(quicksum(a[i][j]*x[j] for j in colonnes) <= b[i], "Contrainte%d" % i)

    # Resolution
    m.optimize()


    print("")                
    print('Solution optimale:')
    for j in colonnes:
        print('x%d'%(j+1), '=', x[j].x)
    print("")
    print('Valeur de la fonction objectif :', m.objVal)

   
