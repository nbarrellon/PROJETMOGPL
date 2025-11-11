from random import randint

def genere_poids(N,M):
    #génère une grille dont chaque case a un poids tiré au hasard entre 1 et 1000
    return [[randint(1,1000) for _ in range(M)] for _ in range(N)]