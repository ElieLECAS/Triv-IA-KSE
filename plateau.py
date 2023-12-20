from random import randint,choice
from pion import Camembert
import os
import time

class Plateau:
    def __init__(self):
        self.categories=['🟥','🟨','🟩','🟦','🟪','🟫']
        self.grille = self.categories *3
        self.largeur_de_la_grille = len(self.grille)
        self.camemberts_disponibles = ["🔴","🔵","🟢","🟣","🟡","🟠",] 
        self.joueurs = []
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
            if joueur.difficulte == "Facile":
                print('rouge Facile')
            if joueur.difficulte == "Intermediaire":
                print('rouge Intermediaire')
            if joueur.difficulte == "Difficle":
                print('rouge Difficle')
            
        elif self.grille[joueur.x] =='🟨':
            if joueur.difficulte == "Facile":
                print('jaune Facile')
            if joueur.difficulte == "Intermediaire":
                print('jaune Intermediaire')
            if joueur.difficulte == "Difficle":
                print('jaune Difficle')

        elif self.grille[joueur.x] =='🟩':
            if joueur.difficulte == "Facile":
                print('vert Facile')
            if joueur.difficulte == "Intermediaire":
                print('vert Intermediaire')
            if joueur.difficulte == "Difficle":
                print('vert Difficle')

        elif self.grille[joueur.x] =='🟦':
            if joueur.difficulte == "Facile":
                print('bleu Facile')
            if joueur.difficulte == "Intermediaire":
                print('bleu Intermediaire')
            if joueur.difficulte == "Difficle":
                print('bleu Difficle')

        elif self.grille[joueur.x] =='🟪':
            if joueur.difficulte == "Facile":
                print('violet Facile')
            if joueur.difficulte == "Intermediaire":
                print('violet Intermediaire')
            if joueur.difficulte == "Difficle":
                print('violet Difficle')

        elif self.grille[joueur.x] =='🟫':
            if joueur.difficulte == "Facile":
                print('marron Facile')
            if joueur.difficulte == "Intermediaire":
                print('marron Intermediaire')
            if joueur.difficulte == "Difficle":
                print('marron Difficle')


    def debut_de_tour(self, joueur):
        os.system('clear')
        joueur.lance_de()                
        valeur_de= joueur.resultat
                
        self.afficher_le_plateau()
        print(f'\nC\'est le tour de {joueur.couleur} {joueur.nom_du_joueur} !\n\nTu as {len(joueur.score)} camemberts\n {joueur.score}\n\n')
        input("\nAppuie sur Entrée pour lancer le dé ! ")

        os.system('clear')
        
        print(f'Le lancer de dé donne  : {valeur_de}\n')
        joueur.deplacer_camembert()
        self.afficher_le_plateau()
        self.attribution_categorie(joueur)


    def questions_reponses(self, joueur):
        if input(f'\nQuestion de niveau {joueur.difficulte} \nParis est la capitale de la France.\na. True   b. False\n\nVotre réponse : \n') == "a":
            os.system('clear')
            print('Bravo ! \n')
            joueur.tot_bonnes_reponses.append(self.grille[joueur.x])
            if len(joueur.score) == 2:
                joueur.difficulte = "Intermediaire"
            elif len(joueur.score) == 4:
                joueur.difficulte = "Difficile"
        else:
            os.system('clear')
            print('Perdu ! \n')

    def fin_de_tour(self, joueur):
        joueur.afficher_score()
        print(joueur.score)   
        self.afficher_le_plateau()
        print(f'\nTu as maintenant {len(joueur.score)} camemberts ! \n')
        input('\nAppuie sur Entrée pour finir le tour !\n')
        
            
    
    def deroulement (self):
        
        self.afficher_le_plateau()
        for joueur in self.joueurs:
            joueur.attribution_couleur_pion()

        while len(joueur.score)<6:
            for joueur in self.joueurs:

                self.debut_de_tour(joueur)
                self.questions_reponses(joueur)
                self.fin_de_tour(joueur)

                if len(joueur.score) == 6:
                    print("Gagné !\n")
                    break
                                
        for joueur in self.joueurs:
            print(f'{joueur.nom_du_joueur} : {sorted(joueur.tot_bonnes_reponses, reverse=True)}\n')
        
            
    
    
        

plateau1 = Plateau()
plateau1.peupler_le_plateau(2)
plateau1.deroulement()






