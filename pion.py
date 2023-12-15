from random import choice
from plateau import Plateau

class Camembert:
    def __init__(self,plateau):
        self.couleur = "⭕"
        self.tot_bonnes_reponses = []
        self.score=set(self.tot_bonnes_reponses)
        self.plateau = plateau
        self.x = random.choice(range(plateau.largeur_de_la_grille))



    # def deplacement (self):
        
