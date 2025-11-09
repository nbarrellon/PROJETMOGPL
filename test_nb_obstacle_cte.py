from calcul_chemin import *
from time import perf_counter
from generation_instance import *

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
            ########### mesure du temps necessaire à l'algorithme #############""
            t0 = perf_counter()
            bfs(g,depart,arrivee)
            t1 = perf_counter()
            tps_moyen += (t1-t0)
            #########################################
    return tps_moyen/10

#creation des fichiers d'instance à tester. 10 instances de N=5 à N=50 (*10 blocs)
for i in range(5,55,5):
    instances = [(i,i,i)]*10
    nom_fichier = "./OUTPUT/instance"+str(i)*3+".txt"
    creation_fichier(instances,nom_fichier,False,(0,0),(i,i),"nord")

temps_necessaire = []
#tests sur instances N=M=10,20,30,40,50 avec nb_obstacles cte. Chaque instance est testée 10 fois

for inst in instances:
    temps_necessaire.append(test_nb_obstacle_cte(inst))

print(temps_necessaire)
############ TRACE DE LA COURBE t = f(N) ###########################""""
import matplotlib.pyplot as plt
import numpy as np


N = [i for i in range(5,51,5)] #abcisse = taille de l'entrée pour une matrice carrée

N_array = np.array(N)
temps_necessaire_array = np.array(temps_necessaire)

# Calcul de la régression linéaire (degré 1)
coefficients = np.polyfit(N_array, temps_necessaire_array, 1)
pente = coefficients[0]
ordonnee_origine = coefficients[1]

# Création de la fonction linéaire
regression_lineaire = np.poly1d(coefficients)

# Création du graphique
plt.figure(figsize=(8, 5))
plt.plot(N, temps_necessaire, marker='o', linestyle='', color='b', label='Données')
plt.plot(N_array, regression_lineaire(N_array), color='r', label=f'Régression linéaire (pente = {pente:.3f})')

# Ajout des labels et titre
plt.xlabel('N')
plt.ylabel('Temps moyen (s)')
plt.title('Courbe du temps moyen en fonction de N avec régression linéaire')
plt.grid(True)
plt.legend()
plt.savefig("instanceX-X-X.png")
# Affichage du graphique
plt.show()
