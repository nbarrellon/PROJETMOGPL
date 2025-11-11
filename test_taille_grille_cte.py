from calcul_chemin import *
from time import perf_counter
from generation_instance import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from scipy.optimize import curve_fit

#on considère qu'il y a 10 instances dans le fichier
def test_taille_grille_cte(fichier):
    points_cardinaux = ["nord","est","sud","ouest"]
    with open(fichier,"r",encoding='utf-8') as f:
        for _ in range(20): #on calcule les chemins pour les 20 instances et on les sauvegarde
            tps_moyen = 0
            ############# Lecture du bloc ######################
            ligne1 = f.readline().split()
            N = int(ligne1[0]) #matrice carrée N = M
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
    return tps_moyen/20

#creation des fichiers d'instance à tester. instances de N=5 à N=50 (*20 blocs)
instances= []
for i in range(10,100,1): #nb obstacle de 10 à 300 par pas de 10
    instance = [(20,20,i)]*20 #grille de 20 par 20 avec i obstacles
    nom_fichier = "./OUTPUT/instance_taille_grille_cte"+str(i)+".txt"
    instances.append(nom_fichier)
    #pour chaque instance, départ et arrivée sont placés aux deux extrémités opposées.
    creation_fichier(instance,nom_fichier,False,(0,0),(i,i),"nord")
print(instances)
temps_necessaire = []

for inst in instances:
    temps_necessaire.append(test_taille_grille_cte(inst))

print(temps_necessaire)
############ TRACE DE LA COURBE t = f(N) ###########################""""
import matplotlib.pyplot as plt
import numpy as np


P = [i for i in range(10,100,1)] #abcisse = taille de l'entrée pour une matrice carrée = nb obstacles

P_array = np.array(P)
temps_necessaire_array = np.array(temps_necessaire)


# Calcul des logarithmes
log_P = np.log(P_array)
log_temps = np.log(temps_necessaire_array)

# Fonction de modélisation pour log(t) = b * log(n) + c
def modele_log(x, b, c):
    return b * x + c

# Ajustement du modèle logarithmique
popt_log, _ = curve_fit(modele_log, P_array, temps_necessaire_array)
b, c = popt_log  # Coefficients trouvés

# Valeurs pour la courbe modélisée en échelle logarithmique
P_fit = np.linspace(min(P), max(P), 100)
temps_fit = modele_log(P_fit, b, c)

# Création des graphiques
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Graphique 1 : t = f(n)
ax1.plot(P, temps_necessaire, 'bo-', label='Données expérimentales')
ax1.set_xlabel("Nombre d'obstacles (P)")
ax1.set_ylabel('Temps nécessaire (t)')
ax1.set_title('Courbe $t = f(P)$')
ax1.legend()
ax1.grid(True)

# Graphique 2 : log(t) = f(log(n))
ax2.plot(P, temps_necessaire, 'bo-', label='Données en échelle logarithmique')
ax2.plot(P_fit, temps_fit, 'r--', label=f'Modélisation : $\\t = {b:.4f} \\cdot \\P$')

ax2.set_xlabel('$\P$')
ax2.set_ylabel('$\t$')
ax2.set_title('Courbe $\\t = f(\\P)$')
ax2.legend()
ax2.grid(True)

# Ajustement de la mise en page
plt.tight_layout()

# Sauvegarde et affichage
plt.savefig("instance_taille_grille_cte.png")
plt.show()
