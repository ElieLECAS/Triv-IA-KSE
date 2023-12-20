from random import choice,randint


class Camembert:
    def __init__(self,plateau):
        self.tot_bonnes_reponses = []
        self.score= ()
        self.plateau = plateau
        self.couleur = None
        self.difficulte = "Facile"
        self.nom_du_joueur= input("quel est votre nom? : ")
        self.x = 0
        self.resultat = None
    
        
    def afficher_score(self):
        self.score=set(self.tot_bonnes_reponses)
        return 
    
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