from Graphe import *
from generation_instance import *
from calcul_chemin import *
from dessin import *

def menu():
    print("\n-------------------------------------")
    print("-------- LA BALADE DU ROBOT ---------")
    print("-------------------------------------")
    print("Que voulez-vous faire ?")
    print("1 -> Générer un fichier d'instances")
    print("2 -> Générer un fichier chemin à partir d'instances")
    print("3 -> Générer une instance et sa solution")
    print("4 -> Sortir")
    choix = int(input("Votre choix ->"))
    return choix

def generation():
    print("--------- Generation d'un fichier instance --------------")
    n = int(input("Combien de blocs ?"))
    instances = []
    for i in range(1,n+1):
        print("----------Bloc n°"+str(i)+" ---------------")
        N = int(input("Que vaut N ? ->"))
        M = int(input("Que vaut M ? ->"))
        P = int(input("Combien d'obstacles ? ->"))
        while P>90*(N*M)/100:
            print("Trop d'obstacles !")
            P = int(input("Combien d'obstacles ? ->"))
            
        instances.append((N,M,P))

    print("------------------------------------")
    fichier = input("Nom du fichier de sauvegarde sans extension ->")
    fichier = "./OUTPUT/"+fichier + ".txt"
    creation_fichier(instances,fichier)
    print("Fichier d'instances créé avec succes dans le dossier OUTPUT")

def solution():
    print("--------- Generation d'un fichier solution --------------")
    fichier = input("Quel est le nom du fichier instance sans extension ? ->")
    nom_fichier = "./OUTPUT/"+fichier+".txt"
    try:
        n = 0
        #on compte le nombre de blocs du fichier instances
        with open(nom_fichier,"r",encoding="utf-8") as f:
            for ligne in f.readlines():
                if ligne=="0 0\n":
                    n+=1
    except FileNotFoundError:
        print("Désolé, le fichier ",fichier," n'existe pas !")
        return
    points_cardinaux = ["nord","est","sud","ouest"]
    chemins = [] #pour stocker les n chemins correspondant aux n blocs
    with open(nom_fichier,"r",encoding='utf-8') as f:
        for _ in range(n): #on calcule les chemins pour les n instances et on les sauvegarde
            ############# Lecture du bloc ######################
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
            ########## Generation du chemin ####################
            g = Graphe(grille)
            orientation = points_cardinaux.index(orientation)
            depart = (D1,D2,orientation)
            arrivee = (F1,F2)
            ########## BFS ##############
            chemin = bfs(g,depart,arrivee)
            ##############################
            if chemin!=-1:
                chemin = ecriture_chemin(chemin,depart,arrivee)
            chemin = traduction_chemin(chemin)
            chemins.append(chemin)
    nom_fichier = "./OUTPUT/"+fichier+"Reponses.txt"
    with open(nom_fichier,"w",encoding='utf-8') as f:
        for c in chemins:
            f.write(c)
    print("Fichier solution créé avec succes dans le dossier OUTPUT")
    
def affichage():
    print("--------- Résolution d'une instance  --------------")
    N = int(input("Que vaut N ? ->"))
    M = int(input("Que vaut M ? ->"))
    P = int(input("Combien d'obstacles ? ->"))
    while P>90*(N*M)/100:
        print("Trop d'obstacles !")
        P = int(input("Combien d'obstacles ? ->"))
    grille = generation_grille(N,M,P)
    depart = (-1,-1)
    arrivee = (-1,-1)
    while not(choix_depart_arrivee(grille,depart)):
        depart = (randint(0,N),randint(0,M))
    deja_essaye = [depart]
    while not(choix_depart_arrivee(grille,arrivee)) or arrivee not in deja_essaye:
        arrivee = (randint(0,N),randint(0,M))
        deja_essaye.append(arrivee)
         
    g = Graphe(grille)
    D1,D2 = depart
    orientation = randint(0,3)
    depart = (D1,D2,orientation)
    chemin = bfs(g,depart,arrivee)
    orientation = ["nord","est","sud","ouest"][orientation]
    if chemin!=-1:
        chemin = ecriture_chemin(chemin,depart,arrivee)
        cheminbis = [(c[0],c[1]) for c in chemin]
        cheminter=[]
        for c in cheminbis:
            if c not in cheminter:
                cheminter.append(c)
    else:
        cheminter=[]
    chemin_affichage = traduction_chemin(chemin)+" depart :"+str(depart)+"arrivée:"+str(arrivee)+"orientation départ :"+orientation
    
    dessiner_grille_intersections(grille,[(D1,D2),arrivee],cheminter,chemin_affichage,orientation)

if __name__=="__main__":
    choix = menu()
    faire = [generation,solution,affichage]
    while choix !=4:
        faire[choix-1]()
        choix = menu()
