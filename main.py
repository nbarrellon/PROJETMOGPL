from Graphe import *
from generation_instance import *
from calcul_chemin import *

def menu():
    print("-------------------------------------")
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
        instances.append((N,M,P))

    print("------------------------------------")
    fichier = input("Nom du fichier de sauvegarde sans extension ->")
    fichier = "./OUTPUT/"+fichier + ".txt"
    creation_fichier(instances,fichier)
    
def solution():
    print("--------- Generation d'un fichier solution --------------")

def affichage():
    print("--------- Résolution d'une instance  --------------")  

if __name__=="__main__":
    choix = menu()
    faire = [generation,solution,affichage]
    while choix !=4:
        faire[choix-1]()


        menu()
