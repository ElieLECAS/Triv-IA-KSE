from random import choice,randint


class Camembert:
    def __init__(self,plateau):
        self.tot_bonnes_reponses = []
        self.score=set(self.tot_bonnes_reponses)
        self.plateau = plateau
        self.couleur = None
        self.difficulte = 1
        self.nom_du_joueur= input("quel est votre nom? : ")
        self.x = 0
    
    def afficher_score(self):
        return self.score
    
    def lance_de(self):
        lance_randint = randint(1,6)
        self.resultat = lance_randint
        return 
        
    def attribution_couleur_pion (self):
        self.couleur = choice(self.plateau.camemberts_disponibles)
        self.plateau.camemberts_disponibles.remove(self.couleur)
        return 
    
    def deplacer_camembert(self):
        resultat_de = self.resultat
        self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille
        # self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille