from calcul_chemin import *

#on considère qu'il y a 10 instances dans le fichier
def test_nb_obstacle_cte(fichier):
    points_cardinaux = ["nord","est","sud","ouest"]
    chemins = [] #pour stocker les 10 chemins correspondant aux 10 blocs
    with open(fichier,"r",encoding='utf-8') as f:
        for _ in range(10): #on calcule les chemins pour les 10 instances et on les sauvegarde
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
            chemin = bfs(g,depart,arrivee)
            if chemin!=-1:
                chemin = ecriture_chemin(chemin,depart,arrivee)
            chemin = traduction_chemin(chemin)
            chemins.append(chemin)
    print(chemins)
    nom_fichier = fichier[:-4]+"Reponses.txt"
    with open(nom_fichier,"w",encoding='utf-8') as f:
        for c in chemins:
            f.write(c)

instances_a_tester=["instance10-10-10.txt","instance20-20-20.txt","instance30-30-30.txt","instance40-40-40.txt","instance50-50-50.txt"]
for inst in instances_a_tester:
    test_nb_obstacle_cte(inst)
