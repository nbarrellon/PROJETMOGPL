*************************************************************************
***************** PROJET MOGPL : LA BALADE DU ROBOT *********************
*************************************************************************

Nils BARRELLON 21401602

Les bibliothèques python Collections, Tkinter, Time, Gurobi, Matplotlib.pyplot, Numpy, Scipy.optimize et Scipy.stats
doivent être installées.

-> lancer main.py avec un interpreteur Python 3.10 ou supérieur

-------- MENU --------------
1 - Générer un fichier d'instances
2 - Générer un fichier chemin à partir d'instances
3 - Générer une instance et sa solution
4 - Générer une instance avec Gurobi et sa solution
5 - Sortir

1) Demande le nombre de blocs de l'instance puis, pour chaque bloc, la taille de la grille (N et M) 
et le nombre d'obstacles P désirés. Demande le nom du fichier de sauvegarde.
Crée alors un fichier dans le dossier OUTPUT de l'instance avec les blocs comme demandé dans l'énoncé.
Les P obstacles sont placés au hasard dans la grille.
Les coordonnees de départ et de l'arrivée sont tirés au hasard dans la grille à des positions correctes.
L'orientation par défaut au départ est tirée au hasard.

2) Demande le nom du fichier d'instance à traiter. Crée alors un fichier nomReponses.txt dans le dossier OUTPUT
qui contient sur chaque ligne les chemins de départ à arrivée (-1 si impossible). Une ligne = un bloc de l'instance.

3) Demande la taille de la grille et le nombre d'obstacle.Génère une instance aléatoire de taille N*M 
contenant P obstacles. Choisit au hasard une orientation et des coordonnées de départ et d'arrivée. Calcule le chemin
de départ à arrivée puis affiche ce chemin sous la forme d'une petite animation avant de l'écrire.
PS : l'interface graphique a été codée par l'IA sous ma supervision (Mistral AI - Le chat)

4) Demande la taille de la grille et le nombre d'obstacle. Génère une grille de taille N*M où
chaque case reçoit un poids entre 1 et 1000 choisi aléatoirement.
Génère une instance de taille N*M contenant P obstacles, placé de telle façon à ce que la somme des cases pondérées
 soit minimale. La position des obstacles respecte aussi les contraintes de l'énoncé.
Choisit au hasard une orientation et des coordonnées de départ et d'arrivée. Calcule le chemin
de départ à arrivée puis affiche ce chemin sous forme graphique dans une grille où les poids des cases apparaissent.
PS : l'interface graphique a été codée par l'IA sous ma supervision (Mistral AI - Le chat)

5) Fin du programme

