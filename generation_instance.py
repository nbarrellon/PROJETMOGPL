from random import randint

def generation_grille(N,M,P):
    nb_obstacle = P
    grille = [[0 for _ in range(M)] for _ in range(N)] #creation grille vierge
    #ajout des P obsctacle
    while nb_obstacle>0:
        x = randint(0,N-1)
        y = randint(0,M-1)
        if grille[x][y]==0:
            nb_obstacle-=1
            grille[x][y]=1
    return grille

def affiche_grille(grille):
    #pour vérifier la création de l'instance
    N = len(grille)
    M = len(grille[0])
    for i in range(N):
        for j in range(M):
            print(grille[i][j],end=" ")
        print()

instance = generation_grille(5,10,7)
affiche_grille(instance)

