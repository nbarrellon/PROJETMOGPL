class Graphe:
    #on implémente le graphe par dictionnaire d'adjacence
    def __init__(self,grille):
        self.graphe=dict()
        direction = [(0,-1),(0,0),(-1,0),(-1,-1)] #pour  correspondance grille<->coordonnées
        self.N = len(grille)
        self.M = len(grille[0])
        #on récupère la liste des sommets à éliminer
        self.obstacles = set()
        for x in range(self.N+1):
            for y in range(self.M+1):
                cases_a_verifier = []
                for d in direction:
                    x_prime = x+d[0]
                    y_prime = y+d[1]
                    if not(x_prime<0 or y_prime<0 or x_prime>=self.N or y_prime>=self.M):
                        cases_a_verifier.append((x_prime,y_prime))
                for case in cases_a_verifier:
                    if grille[case[0]][case[1]]==1:
                        self.obstacles.add((x,y)) #on ajoute pas ce sommet
        print("obstacles : ",self.obstacles)
        #construction du graphe
        for x in range(self.N+1):
            for y in range(self.M+1):
                if (x,y) not in self.obstacles:#on vérifie si le sommet existe
                    for orientation in range(4):
                        etat = (x, y, orientation)
                        self.graphe[etat]=[]
                        # Ajouter les sommets orientés 
                        # et les arcs "Tourne" a droite" et "Tourne à gauche"
                        for d in [-1, 1]:
                            new_orientation = (orientation + d) % 4
                            self.graphe[etat].append((x, y, new_orientation))
                        # Ajouter les arcs pour "Avance(n)"
                        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Nord, Est, Sud, Ouest
                        dx, dy = directions[orientation]
                        nx, ny = x + dx, y + dy
                        #on teste si on est en bord de grille et si le sommet n'est pas empêché
                        if 0 <= nx <= self.N and 0 <= ny <= self.M and (nx, ny) not in self.obstacles:
                            self.graphe[etat].append((nx, ny, (orientation+2)%4))

    def __str__(self):
        ch = ""
        for sommet in self.graphe:
            ch += str(sommet)+":"+str(self.graphe[sommet])+"\n"
        return ch
                            
    def voisins(self,sommet):
        return self.graphe[sommet]


