from random import randint,choice
# from pion import Camembert

class Plateau:
    def __init__(self, largeur_de_la_grille):
        self.largeur_de_la_grille = largeur_de_la_grille
        self.grille = ['🟥','🟨','🟩','🟦','🟪','🟫']
        # self.grille = [0 for case in range(self.largeur_de_la_grille)]
        self.camemberts_disponibles = ["🔴","🔵","🟢","🟣","🟡","🟠",] 
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
            
class Camembert:
    def __init__(self,plateau):
        self.tot_bonnes_reponses = []
        self.score=set(self.tot_bonnes_reponses)
        self.plateau = plateau
        self.couleur = choice(self.plateau.camemberts_disponibles)
        self.difficulte = 1
        self.x = choice(range(plateau.largeur_de_la_grille))
    
    def afficher_score(self):
        return self.score
    
    def deplacer_camembert(self):
        resultat_de = self.plateau.lance_de()
        self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille

    

plateau1 = Plateau(6)
plateau1.peupler_le_plateau(1)
plateau1.afficher_le_plateau()
plateau1.lance_de()
camembert1=Camembert(plateau1)