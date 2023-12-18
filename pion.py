from random import choice


class Camembert:
    def __init__(self,plateau):
        self.tot_bonnes_reponses = []
        self.score=set(self.tot_bonnes_reponses)
        self.plateau = plateau
        self.couleur = None
        self.difficulte = 1
        self.x = choice(range(plateau.largeur_de_la_grille))
    
    def afficher_score(self):
        return self.score
    
    def deplacer_camembert(self):
        resultat_de = self.plateau.resultat
        self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille
        
    def attribution_couleur (self):
        self.couleur = choice(self.plateau.camemberts_disponibles)
        self.plateau.camemberts_disponibles.remove(self.couleur)
        # for choix in self.plateau.camemberts_disponibles:
        #     if self.couleur == choix:
        #         self.plateau.camemberts_disponibles.remove(choix)
        return 
    
