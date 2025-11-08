from Grapheter import *
from generation_instance import *
from collections import deque

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

def bfs(graphe,depart,arrivee):
    visited = []
    chemin = dict() #on cree un dictionnaire successeur:predecesseur pour retrouver le chemin
    p = deque() #creation d'une pile pour le parcours
    p.append(depart)
    trouve = False
    vague = 1
    while p: #on continue jusqu'à l'arrivée ou la fin du parcours
        sommet = p.pop()
        print("vague N°",vague)
        for v in graphe.voisins(sommet):
            if ((v[0],v[1]))==arrivee: #si on trouve le sommet arrivée, qu'importe l'orientation, on arrete.
                trouve = True
                chemin[arrivee]=sommet
                return chemin
            if v not in visited:
                visited.append(v)
                chemin[v]=sommet #pour retrouver en remontant le chemin de l'arrivee jusqu'au départ
                p.append(v)
        print(visited)
        print(chemin)
        vague +=1
    return -1 #on a pas trouvé le sommet arrivée (il n'est pas accessible depuis le départ)

def ecriture_chemin(path,depart,arrivee):
    chemin = [arrivee]
    next = path[arrivee]
    while next!=depart:
        chemin.append(next)
        next = path[next]
    chemin.append(depart)
    return chemin[::-1]


grille,D1,D2,F1,F2,orientation = lecture_fichier_instance("essai2.txt")
points_cardinaux = ["nord","est","sud","ouest"]
orientation = points_cardinaux.index(orientation)
g = Graphe(grille)
#print(g)
depart = (D1,D2,orientation)
print("Depart : ",depart)
arrivee = (F1,F2)
print("Arrivée :",arrivee)
print(g.voisins((0,0,2)))
#chemin = bfs(g,depart,arrivee)
#print(chemin)
#print(ecriture_chemin(chemin,depart,arrivee))
