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
