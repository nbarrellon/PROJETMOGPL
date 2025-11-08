from Graphe import *
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
    p = deque() #creation d'une file pour le parcours
    p.append(depart)
    trouve = False
    vague = 1
    while p: #on continue jusqu'à l'arrivée ou la fin du parcours
        sommet = p.popleft() #on défile
        for v in graphe.voisins(sommet):
            if ((v[0],v[1]))==arrivee: #si on trouve le sommet arrivée, qu'importe l'orientation, on arrete.
                trouve = True
                chemin[arrivee]=sommet
                return chemin
            if v not in visited:
                visited.append(v)
                chemin[v]=sommet #pour retrouver en remontant le chemin de l'arrivee jusqu'au départ
                p.append(v)
    return -1 #on a pas trouvé le sommet arrivée (il n'est pas accessible depuis le départ)

def ecriture_chemin(path,depart,arrivee):
    """
    Entrée : le dictionnaire du bfs où chaque clé est un sommet et sa valeur son prédecesseur
    Sortie : une liste contenant le chemin pour aller de départ à arrivée (x,y,orientation)
    """
    chemin = [arrivee]
    next = path[arrivee]
    while next!=depart:
        chemin.append(next)
        next = path[next]
    chemin.append(depart)
    return chemin[::-1]

def traduction_chemin(path):
    """
    Entrée : le chemin de départ à arrivée dans le graphe
    Sortie : la traduction en D a3 G a1 pour le fichier de sortie
    """
    print(path)
    chemin = str(len(path)-2) #on ote depart et arrivee
    for i in range(len(path)-1):
        x,y,orientation = path[i]
        next_x,next_y,next_orientation = path[i+1]
        if (x,y)==(next_x,next_y): #si les coordonnees sont égales, on tourne
            if next_orientation-orientation==1 or next_orientation-orientation==-3: #le robot a tourné à droite
                chemin += "D "
            else:
                chemin += "G "
        else: #sinon on a avancé
            dx = abs(next_x-x)
            dy = abs(next_y-y)
            #l'un des deux deltas est nul, pas de déplacement en diagonale
            chemin += "a"+str(max(dy,dy))+" "
    return chemin

grille,D1,D2,F1,F2,orientation = lecture_fichier_instance("essai2.txt")
points_cardinaux = ["nord","est","sud","ouest"]
orientation = points_cardinaux.index(orientation)
g = Graphe(grille)
depart = (D1,D2,orientation)
print("Depart : ",depart)
arrivee = (F1,F2)
print("Arrivée :",arrivee)
chemin = bfs(g,depart,arrivee)
chemin = ecriture_chemin(chemin,depart,arrivee)
print(traduction_chemin(chemin))