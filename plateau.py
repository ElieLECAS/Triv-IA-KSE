from random import randint,choice
from pion import Camembert
# from le_de import Dice
import os
import time

class Plateau:
    def __init__(self):
        self.categories=['🟥','🟨','🟩','🟦','🟪','🟫']
        self.triangle_camembert=['🟥','🟨','🟩','🟦','🟪','🟫']
        self.grille = self.categories *3
        self.largeur_de_la_grille = len(self.grille)
        self.camemberts_disponibles = ["🔴","🔵","🟢","🟣","🟡","🟠",] 
        self.joueurs = []
        # self.de = [Dice(self)]
        self.tableau_de_scores = []
       
 

    def peupler_le_plateau(self, nombre_de_joueurs):
        self.joueurs = [Camembert(self) for joueur in range(nombre_de_joueurs)]
        # joueur est une variable pour représenter chaque objet de la classe Camembert  lors la boucle for joueur. A chaque itération, joueur prend
        # la valeur d'un objet Camembert dans la lsite self.joeurs

    def afficher_le_plateau(self):

        for index, ligne in enumerate(self.grille):
            for joueur in self.joueurs:
                if joueur.x == index:
                    ligne += f" {joueur.couleur} {joueur.nom_du_joueur}"
            print(ligne)
    
    def attribution_categorie(self,joueur):

        if self.grille[joueur.x] =='🟥':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass
        elif self.grille[joueur.x] =='🟨':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass
        elif self.grille[joueur.x] =='🟩':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass
        elif self.grille[joueur.x] =='🟦':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass
        elif self.grille[joueur.x] =='🟪':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass
        elif self.grille[joueur.x] =='🟫':
            if joueur.difficulte == 1:
                pass
            if joueur.difficulte == 2:
                pass
            if joueur.difficulte == 3:
                pass
            pass



                    
    
    def deroulement (self):
        
        plateau1.afficher_le_plateau()
        for joueur in self.joueurs:
            joueur.attribution_couleur_pion()
        # for tour in range (200):
        while len(joueur.score)<6:
            for joueur in self.joueurs:
                os.system('clear')
                joueur.lance_de()                
                valeur_de= joueur.resultat
                print(f'\nC\'est le tour de {joueur.nom_du_joueur} !\nTu as {len(joueur.score)} camemberts\n')
                plateau1.afficher_le_plateau()
                input("\nAppuie sur Entrée pour lancer le dé ! ")

                os.system('clear')
                
                print(f'Le lancer de dé donne  : {valeur_de}\n')
                joueur.deplacer_camembert()
                plateau1.afficher_le_plateau()

                if input(f'\nQuestion de niveau {joueur.difficulte} \nParis est la capitale de la France.\na. True   b. False\n\nVotre réponse : \n') == "a":
                    os.system('clear')
                    print('Bravo ! \n')
                    joueur.tot_bonnes_reponses.append(self.grille[joueur.x])
                    if len(joueur.score) :
                        joueur.difficulte += 1
                    elif len(joueur.score) == 4:
                        joueur.difficulte += 1
                else:
                    os.system('clear')
                    print('Perdu ! \n')

                print(joueur.tot_bonnes_reponses)
                joueur.afficher_score()
                print(joueur.score)   
                plateau1.afficher_le_plateau()
                print(f'\nTu as maintenant {len(joueur.score)} camemberts ! \n')
                input('\nAppuie sur Entrée pour finir le tour !\n')
            
    
    
        

plateau1 = Plateau()
plateau1.peupler_le_plateau(2)
plateau1.deroulement()






