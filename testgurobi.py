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
    
    # Matrice des contraintes a 
    a = []
    variables = [1]*M
    for i in range(N):
        a.append([0]*i*M+variables+[0]*(N*M-((i+1)*M))) #contraintes sur les lignes
    #contraintes sur les colonnes
    for j in range(M):
        colonne = []
        for i in range(N*M):
            if i%M==j:
                colonne.append(1)
            else:
                colonne.append(0)
        a.append(colonne)

# Second membre
    b = [2*P/M for _ in range(M)] #seconde membre contraintes lignes
    b += [2*P/N for _ in range(N)] #second membre contraintes colonnes

    return a,b


grille_poids = genere_poids(3,3)
P = 3
print("Grille des poids")
affiche_matrice(grille_poids,3,3)
print("Grille des contraintes")
contraintes,secondmb = resolution_grille(grille_poids,P,3,3)
print(contraintes)
print(secondmb)

