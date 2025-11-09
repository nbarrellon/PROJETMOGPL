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

def dans_la_grille(grille,coordonnees):
    #test : les coordonnées sont-elles dans la grille ?
    x,y = coordonnees
    if x<0 or x>=len(grille):
        return False
    if y<0 or y>=len(grille[0]):
        return False
    return True

def sur_les_rails(grille,coordonnees):
    #test : les coordonnées sont-elles dans la grille ?
    x,y = coordonnees
    if x<0 or x>len(grille):
        return False
    if y<0 or y>len(grille[0]):
        return False
    return True

def choix_depart_arrivee(grille,coordonnees):
    #renvoie True si la coordonnée (x,y) dans la grille est accessible au robot
    x,y = coordonnees
    if not(sur_les_rails(grille,coordonnees)):
        return False
    direction = [(0,-1),(0,0),(-1,0),(-1,-1)]
    cases_a_verifier = []
    for d in direction:
        x_prime = x+d[0]
        y_prime = y+d[1]
        if dans_la_grille(grille,(x_prime,y_prime)):
            cases_a_verifier.append((x_prime,y_prime))
    #verifie que la coordonnée est accessible (pas d'obstacle)
    for case in cases_a_verifier:
        if grille[case[0]][case[1]]==1:
            return False
    return True

def creation_fichier(instances_voulues,fichier,aleatoire=True,depart=(-1,-1),arrivee=(-1,-1),cardinal="nord"):
    """
    Entrée : fichier : nom pour le fichier de sauvegarde
            instances_voulues : liste des instances à générér. Tuple (N,M,P)
    Cree un fichier .txt avec les instances
    Sortie : None
    """
    orientation = ['nord','est','sud','ouest']
    with open(fichier,"w",encoding='utf-8') as f:
        for instance in instances_voulues:
            N,M,P = instance
            grille = generation_grille(N,M,P)
            f.write(str(N)+" "+str(M)+"\n")
            for i in range(N):
                for j in range(M):
                    f.write(str(grille[i][j])+" ")
                f.write("\n")
            if aleatoire:
                while not(choix_depart_arrivee(grille,depart)):
                    depart = (randint(0,N),randint(0,M))
                deja_essaye = [depart]
                while not(choix_depart_arrivee(grille,arrivee)) or arrivee in deja_essaye:
                    arrivee = (randint(0,N),randint(0,M))
                    deja_essaye.append(arrivee)
                cardinal = orientation[randint(0,3)]
            f.write(str(depart[0])+" "+str(depart[1])+" "+str(arrivee[0])+" "+str(arrivee[1])+" "+cardinal+"\n")
            f.write("0 0\n")

if __name__=="__main__":

    for i in range(1,9):
        instances = [(i*10,i*10,i*10)]*i*10
        nom_fichier = "instance"+str(i*10)+"-"+str(i*10)+"-"+str(i*10)+".txt"
        creation_fichier(instances,nom_fichier)


