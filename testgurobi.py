from random import randint

def affiche_matrice(matrice,N,M):
    for i in range(N):
        for j in range(M):
            print(matrice[i][j],end=' ')
        print()

def genere_poids(N,M):
    #génère une grille dont chaque case a un poids tiré au hasard entre 1 et 1000
    return [[randint(1,1000) for _ in range(M)] for _ in range(N)]

def resolution_grille(grille,P,N,M):
    
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

    return a,b


grille_poids = genere_poids(10,10)
P = 10
print("Grille des poids")
affiche_matrice(grille_poids,10,10)
print("Grille des contraintes")
contraintes,secondmb = resolution_grille(grille_poids,P,10,10)
print(contraintes)
print(secondmb)

