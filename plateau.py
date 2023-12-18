from random import randint,choice
from pion import Camembert
import os
import time

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
                os.system('clear')
                plateau1.lance_de()
                valeur_de= self.resultat
                print(f'Le lancer du joueur: {valeur_de}')
                joueur.deplacer_camembert()
                plateau1.afficher_le_plateau()
                time.sleep(2)
            print(tour)
        

plateau1 = Plateau()
plateau1.peupler_le_plateau(2)
plateau1.deroulement()





