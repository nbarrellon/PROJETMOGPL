from random import randint

def affiche_matrice(matrice,N,M):
    for i in range(N):
        for j in range(M):
            print(matrice[i][j],end=' ')
        print()

def genere_poids(N,M):
    #génère une grille dont chaque case a un poids tiré au hasard entre 1 et 1000
    return [[randint(1,1000) for _ in range(M)] for _ in range(N)]

def resolution_grille(P,N,M):
    
    # Matrice des contraintes a 
    a = []
    aff=[]
    variables = [1]*M
    for i in range(N):
        a.append([0]*i*M+variables+[0]*(N*M-((i+1)*M))) #contraintes sur les lignes
        aff.append([0]*i*M+variables+[0]*(N*M-((i+1)*M)))
    print("Contraintes sur les lignes")
    affiche_matrice(aff,N,N*M)
    #contraintes sur les colonnes
    aff= []
    for j in range(M):
        colonne = []
        for i in range(N*M):
            if i%M==j:
                colonne.append(1)
            else:
                colonne.append(0)
        a.append(colonne)
        aff.append(colonne)
    print("Contraintes sur les colonnes")
    affiche_matrice(aff,M,M*N)
    aff = []
    #contraintes sur le 101 pour les lignes
    for i in range(N):
        for j in range(M-2):
            ligne = [0]*N*M
            ligne[j+i*M]=1
            ligne[j+2+i*M]=1
            a.append(ligne)
            aff.append(ligne)
    print("Contraintes 101 sur les lignes")
    print(aff)
    aff = []
    #contraintes 101 pour les colonnes FAUX !!!!
    for i in range(0,N-2):
        for j in range(M):
            ligne = [0]*N*M
            ligne[j+i*M]=1
            ligne[j+2*M+i*M]=1
            a.append(ligne)
            aff.append(ligne)
    print("Contraintes 101 sur les colonnes")
    print(aff)

# Second membre
    b = [2*P/M for _ in range(M)] #seconde membre contraintes lignes
    b += [2*P/N for _ in range(N)] #second membre contraintes colonnes
    b += [2 for _ in range(N*(M-2))]
    b += [2 for _ in range(M*(N-2))]

    return a,b

def affichage_contrainte(contraintes,smb,N,M):
    for i in range(len(contraintes)):
        ch = ""
        for j in range(len(contraintes[i])):
            if contraintes[i][j]:
                ch += "x"+str(j//N)+str(j%M)+"+"
        ch=ch[:-1]+"<="+str(smb[i])
        print(ch)


def fonction_objectif(grille_poids,N,M):
    fonction_obj = []
    for i in range(N):
        for j in range(M):
            fonction_obj.append(grille_poids[i][j])
    #affichage
    ch = "min z="
    for i in range(len(fonction_obj)):
        ch += str(fonction_obj[i])+"*x"+str(i//N)+str(i%M)+"+"
    print(ch[:-1])

N=4
M=4
grille_poids = genere_poids(N,M)
P = 3
print("Grille des poids")
affiche_matrice(grille_poids,N,M)

contraintes,secondmb = resolution_grille(P,N,M)
affichage_contrainte(contraintes,secondmb,N,M)
fonction_objectif(grille_poids,N,M)

