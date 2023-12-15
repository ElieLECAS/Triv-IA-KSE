class Plateau:
    def __init__(self, largeur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.grille = ['🟥','🟨','🟩','🟦','🟪','🟫']
        # self.grille = [0 for case in range(self.largeur_de_la_grille)]
        self.joueurs = []
        self.tableau_de_scores = []

    def peupler_le_plateau(self, nombre_de_joueurs):
        self.joueurs = [Plateau(self) for joueur in range(nombre_de_joueurs)]

    def afficher_le_plateau(self):
        for ligne in self.grille:
            print(ligne)

plateau1 = Plateau(6)
plateau1.afficher_le_plateau()