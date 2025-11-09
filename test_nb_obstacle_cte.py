from calcul_chemin import *
from time import perf_counter
from generation_instance import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

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
instances= []
for i in range(5,35,5):
    instance = [(i,i,i)]*10
    nom_fichier = "./OUTPUT/instance"+str(i)*3+".txt"
    instances.append(nom_fichier)
    #pour chaque instance, départ et arrivée sont placés aux deux extrémités opposées.
    creation_fichier(instance,nom_fichier,False,(0,0),(i,i),"nord")
print(instances)
temps_necessaire = []

for inst in instances:
    temps_necessaire.append(test_nb_obstacle_cte(inst))

print(temps_necessaire)
############ TRACE DE LA COURBE t = f(N) ###########################""""
import matplotlib.pyplot as plt
import numpy as np


N = [i for i in range(5,35,5)] #abcisse = taille de l'entrée pour une matrice carrée

N_array = np.array(N)
temps_necessaire_array = np.array(temps_necessaire)


# Fonction de modélisation : t = a * n^2
def modele_quadratique(n, a):
    return a * n**2

# Ajustement du modèle aux données
popt, pcov = curve_fit(modele_quadratique, N, temps_necessaire)
a = popt[0]  # Coefficient trouvé

# Valeurs pour la courbe modélisée
N_fit = np.linspace(min(N), max(N), 100)
temps_fit = modele_quadratique(N_fit, a)

# Tracé de la courbe
plt.figure(figsize=(10, 6))
plt.plot(N, temps_necessaire, 'bo-', label='Données expérimentales')
plt.plot(N_fit, temps_fit, 'r--', label=f'Modélisation : $t = {a:.4f} \\cdot n^2$')
plt.xlabel('Taille de l\'entrée (N)')
plt.ylabel('Temps nécessaire (t)')
plt.title('Courbe $t = f(n)$ avec modélisation quadratique')
plt.legend()
plt.grid(True)

# Affichage des courbes
plt.tight_layout()
plt.savefig("instanceXXX.png")
# Affichage du graphique
plt.show()
