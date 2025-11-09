from calcul_chemin import *
from time import perf_counter
from generation_instance import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

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
for i in range(5,55,5):
    instance = [(i,i,i)]*10
    nom_fichier = "./OUTPUT/instance"+str(i)*3+".txt"
    instances.append(nom_fichier)
    creation_fichier(instance,nom_fichier,False,(0,0),(i,i),"nord")
print(instances)
temps_necessaire = []

for inst in instances:
    temps_necessaire.append(test_nb_obstacle_cte(inst))

print(temps_necessaire)
############ TRACE DE LA COURBE t = f(N) ###########################""""
import matplotlib.pyplot as plt
import numpy as np


N = [i for i in range(5,55,5)] #abcisse = taille de l'entrée pour une matrice carrée

N_array = np.array(N)
temps_necessaire_array = np.array(temps_necessaire)





# Calcul des logarithmes (base 10)
log_N = np.log10(N_array)
log_temps = np.log10(temps_necessaire_array)

# Régression linéaire sur log(t) = f(log(n))
slope, intercept, r_value, p_value, std_err = linregress(log_N, log_temps)

# Création de la figure avec deux sous-graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Première courbe : t = f(n)
ax1.plot(N, temps_necessaire, 'bo-', label='Données')
ax1.set_xlabel('N')
ax1.set_ylabel('Temps nécessaire (t)')
ax1.set_title('Courbe t = f(n)')
ax1.grid(True)

# Deuxième courbe : log(t) = f(log(n)) avec régression linéaire
ax2.plot(log_N, log_temps, 'ro-', label='Données')
ax2.plot(log_N, slope * log_N + intercept, 'g--', label=f'Régression linéaire (pente = {slope:.3f})')
ax2.set_xlabel('log(N)')
ax2.set_ylabel('log(Temps nécessaire)')
ax2.set_title('Courbe log(t) = f(log(n)) avec régression linéaire')
ax2.legend()
ax2.grid(True)

# Affichage des courbes
plt.tight_layout()
plt.savefig("instanceXXX.png")
# Affichage du graphique
plt.show()
