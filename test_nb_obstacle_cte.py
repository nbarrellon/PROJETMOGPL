from calcul_chemin import *
from time import perf_counter


#on considère qu'il y a 10 instances dans le fichier
def test_nb_obstacle_cte(fichier):
    points_cardinaux = ["nord","est","sud","ouest"]
    chemins = [] #pour stocker les 10 chemins correspondant aux 10 blocs
    with open(fichier,"r",encoding='utf-8') as f:
        for _ in range(10): #on calcule les chemins pour les 10 instances et on les sauvegarde
            tps_moyen = 0
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
            t0 = perf_counter()
            chemin = bfs(g,depart,arrivee)
            t1 = perf_counter()
            tps_moyen += (t1-t0)
            if chemin!=-1:
                chemin = ecriture_chemin(chemin,depart,arrivee)
            chemin = traduction_chemin(chemin)
            chemins.append(chemin)
    nom_fichier = fichier[:-4]+"Reponses.txt"
    with open(nom_fichier,"w",encoding='utf-8') as f:
        for c in chemins:
            f.write(c)
    return tps_moyen/10
    
temps_necessaire = []
#tests sur instances N=M=10,20,30,40,50 avec nb_obstacles cte. Chaque instance est testée 10 fois
instances_a_tester=["instance10-10-10.txt","instance20-20-20.txt","instance30-30-30.txt","instance40-40-40.txt","instance50-50-50.txt"]
for inst in instances_a_tester:
    temps_necessaire.append(test_nb_obstacle_cte(inst))

############ TRACE DE LA COURBE t = f(N) ###########################""""
import matplotlib.pyplot as plt

# Exemple de données (remplacez par vos listes)
N = [10, 20, 30, 40, 50]
temps_moyen = [0.5, 1.2, 2.1, 3.0, 4.3]

# Création du graphique
plt.figure(figsize=(8, 5))
plt.plot(N, temps_moyen, marker='o', linestyle='-', color='b', label='Temps moyen')

# Ajout des labels et titre
plt.xlabel('N')
plt.ylabel('Temps moyen (s)')
plt.title('Courbe du temps moyen en fonction de N - Nb obstacle constant')
plt.grid(True)
plt.legend()
plt.savefig("instanceX-X-X.png")
# Affichage du graphique
plt.show()
