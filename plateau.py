from random import randint,choice
# from pion import Camembert

class Plateau:
    def __init__(self):
        self.largeur_de_la_grille = 6
        self.grille = ['🟥','🟨','🟩','🟦','🟪','🟫']
        # self.grille = [0 for case in range(self.largeur_de_la_grille)]
        self.camemberts_disponibles = ["🔴","🔵","🟢","🟣","🟡","🟠",] 
        self.joueurs = []
        self.tableau_de_scores = []
        self.resultat= 0
 

    def peupler_le_plateau(self, nombre_de_joueurs):
        self.joueurs = [Camembert(self) for joueur in range(nombre_de_joueurs)]
        # joueur est une variable pour représenter chaque objet de la classe Camembert  lors la boucle for joueur. A chaque itération, joueur prend
        # la valeur d'un objet Camembert dans la lsite self.joeurs

    def afficher_le_plateau(self):

        for index, ligne in enumerate(self.grille):
            for joueur in self.joueurs:
                if joueur.x == index:
                    ligne += f" {joueur.couleur}"
            print(ligne)
                       

    def lance_de(self):
            lance_randint = randint(1,6)
            self.resultat = lance_randint
            return 
    
    def deroulement (self):
        plateau1.peupler_le_plateau(2)
        plateau1.afficher_le_plateau()
        for tour in range (1,6):
            for joueur in self.joueurs:
                plateau1.lance_de()
                valeur_de= self.resultat
                print(f'Le lancer du joueur: {valeur_de}')
                joueur.deplacer_camembert()
                plateau1.afficher_le_plateau()
            print(tour)

            
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
        resultat_de = self.plateau.resultat
        self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille
    
    # def deplacer_camembert(self):
    #     resultat_de = self.plateau.lance_de()
    #     self.x = (self.x + resultat_de) % self.plateau.largeur_de_la_grille
        

plateau1 = Plateau()
plateau1.peupler_le_plateau(2)
plateau1.deroulement()





# plateau1 = Plateau(6)
# plateau1.peupler_le_plateau(1)
# camembert1=Camembert(plateau1)
# plateau1.afficher_le_plateau()
# plateau1.lance_de()
# camembert1.deplacer_camembert()
# camembert1.deplacer_camembert()
# camembert1.afficher_score()
# plateau1.afficher_le_plateau()