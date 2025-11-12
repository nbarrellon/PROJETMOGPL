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
    #derniere contrainte : il faut qu'il y ait P obstacles 
    #sinon pour minimiser c'est facile, on ne prend rien !
    a.append([-1]*N*M) #*-1 pour <=

# Second membre
    b = [2*P/M for _ in range(M)] #seconde membre contraintes lignes
    b += [2*P/N for _ in range(N)] #second membre contraintes colonnes
    b += [1 for _ in range(N*(M-2))]
    b += [1 for _ in range(M*(N-2))]
    b.append(-P) #il faut P obstacles ! On *-1 pour avoir un <=
    return a,b

def affichage_contrainte(contraintes,smb,N,M):
    for i in range(len(contraintes)):
        ch = ""
        for j in range(0,len(contraintes[i])):
            if contraintes[i][j]:
                ch += "x"+str(j+1)+"+"
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
        ch += str(fonction_obj[i])+"*x"+str(i+1)+"+"
    #print(ch[:-1])
    return fonction_obj

def brute_force(grille,N,M,P): #trouver les solutions de poids minimal
    #COMPLEXITE EXPONENTIELLE ! Et ne prend pas en compte les contraintes sur le nombre d'obstacle max par ligne
    instance = []
    for g in grille:
        instance+=g #on aplatit la matrice
    solutions = set()
    for inst in range(2**P-1,2**(N*M)): #toutes les solutions ayant au moins P bits à 1
        solution = str(bin(inst))[2:]
        solution = "0"*(N*M-len(solution))+solution
        if solution.count("1")==P: #on ne garde que les solutions qui ont P bits à 1
            solutions.add(solution)
    mini = 1000*P #plus grand valeur de la somme possible
    res = ""
    for sol in solutions:
        s = 0
        for i in range(len(sol)):
            s += instance[i]*int(sol[i])
            #print(s)
        if s<mini:
            mini = s
            res = sol
    print("Solution = ",res," pour un cout de ",mini)


#####################################################################*
if __name__=="__main__":
    N=5
    M=5
    grille_poids = genere_poids(N,M)
    P = 5

    affiche_matrice(grille_poids,N,M)
    contraintes,secondmb = resolution_grille(P,N,M)
    f_obj = fonction_objectif(grille_poids,N,M)
    affichage_contrainte(contraintes,secondmb,N,M)


