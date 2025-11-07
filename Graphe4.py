from collections import defaultdict

class GrapheRobot:
    def __init__(self, N, M, obstacles):
        self.N = N
        self.M = M
        self.obstacles = obstacles
        self.graphe = defaultdict(list)
        self.directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # Nord, Est, Sud, Ouest

    def ajouter_arc(self, etat_depart, etat_arrivee):
        self.graphe[etat_depart].append(etat_arrivee)

    def construire_graphe(self):
        for x in range(self.N):
            for y in range(self.M):
                for orientation in range(4):
                    etat = (x, y, orientation)
                    # Ajouter les arcs pour "Tourne"
                    for d in [-1, 1]:
                        new_orientation = (orientation + d) % 4
                        self.ajouter_arc(etat, (x, y, new_orientation))
                    # Ajouter les arcs pour "Avance(n)"
                    for n in [1, 2, 3]:
                        dx, dy = self.directions[orientation]
                        nx, ny = x + n*dx, y + n*dy
                        if 0 <= nx < self.N and 0 <= ny < self.M and (nx, ny) not in self.obstacles:
                            self.ajouter_arc(etat, (nx, ny, orientation))
