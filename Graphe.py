class Graphe:
    #on implémente le graphe par dictionnaire d'adjacence
    def __init__(self,grille):
        self.graphe=dict()
        direction = [(0,-1),(0,0),(-1,0),(-1,-1)]
        orientation = ["N","E","S","O"]
        N = len(grille)
        M = len(grille[0])
        #on récupère la liste des sommets à éliminer
        self.obstacles = []
        for x in range(N):
            for y in range(M):
                cases_a_verifier = []
                for d in direction:
                    x_prime = x+d[0]
                    y_prime = y+d[1]
                    if not(x_prime<0 or y_prime<0 or x_prime>=N or y_prime>=M):
                        cases_a_verifier.append((x_prime,y_prime))
                for case in cases_a_verifier:
                    if grille[case[0]][case[1]]==1:
                        self.obstacles.append((x,y)) #on ajoute pas ce sommet
        print("obstacles : ",self.obstacles)
   


