from random import randint
from pion import Camembert

class Plateau:
    def __init__(self, largeur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.grille = ['🟥','🟨','🟩','🟦','🟪','🟫']
        # self.grille = [0 for case in range(self.largeur_de_la_grille)]
        self.joueurs = []
        self.tableau_de_scores = []

    def peupler_le_plateau(self, nombre_de_joueurs):
        self.joueurs = [Camembert(self) for joueur in range(nombre_de_joueurs)]
        # il y a autant de camemebert que de joueur 

    def afficher_le_plateau(self):
        for ligne in self.grille:
            print(ligne)

    def lance_de(self):
            resultat = randint(1,6)
            print(f'Le lancer du dé donne : {resultat}')
            return resultat
            
    

plateau1 = Plateau(6)
plateau1.peupler_le_plateau(1)
plateau1.afficher_le_plateau()
plateau1.lance_de()


