from random import randint,choice
from pion import Camembert
from mysqlHandler import MySQLHandler
import os
import time


class Plateau:
    def __init__(self,access):
        self.categories=['🟥','🟨','🟩','🟦','🟪','🟫']
        self.grille = self.categories *3
        self.largeur_de_la_grille = len(self.grille)
        self.camemberts_disponibles = ["🔴","🔵","🟢","🟣","🟡","🟠",] 
        self.joueurs = []
        self.tableau_de_scores = []
        self.access= access
           
       
 

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

        
        dico = {'🟥' : 'SQL' , '🟨' :'Python' , '🟩' : 'Ligne de commandes' , '🟦' : 'Actualités IA' , '🟪' : 'Git/Github' , '🟫' : 'Thème mystère'}    
        
        for carre, categorie in dico.items():
            difficulte = joueur.difficulte
            
            if self.grille[joueur.x] == carre:
                params=(categorie,difficulte)
                return params


    def debut_de_tour(self, joueur):
        os.system('clear')
        joueur.lance_de()                
        valeur_de= joueur.resultat
                
        self.afficher_le_plateau()
        print(f'\nC\'est le tour de {joueur.couleur} {joueur.nom_du_joueur} !\n\nTu as {len(joueur.score)} camemberts\n {" ".join(joueur.score)}\n\n')
        input("\nAppuie sur Entrée pour lancer le dé ! ")

        os.system('clear')
        joueur.deplacer_camembert()
        self.afficher_le_plateau()
        print(f'Le lancer de dé donne  : {valeur_de}\n')
        


    def questions_reponses(self, joueur):
        params = self.attribution_categorie(joueur)
        question = self.access.read_questions(params)

        print (f"{' '.join(joueur.score)}\n\n")

        if question:  # Vérifiez si la liste de questions n'est pas vide
            question = question[0]  # Prenez la première question de la liste
            print(f"Catégorie : {params[0]}\nNiveau : {params[1]}\n")
            print(question)
            return_reponse = self.access.bonne_reponse(question)

            user_input = input()
            if user_input == return_reponse:
                os.system('clear')
                print(f'Bravo {joueur.nom_du_joueur}!\n\n')
                joueur.tot_bonnes_reponses.append(self.grille[joueur.x])
                if len(joueur.score) == 2:
                    joueur.difficulte = "Intermediaire"
                elif len(joueur.score) == 4:
                    joueur.difficulte = "Difficile"
            else:
                os.system('clear')
                print('Perdu ! \n\n')
                print(f"{question}\n")
                print(f" La bonne réponse était {return_reponse}\n\n")

            joueur.tot_reponses_repondues.append(self.grille[joueur.x])
        else:
            os.system('clear')
            print("Aucune question disponible pour cette catégorie et difficulté.")
            


    def fin_de_tour(self, joueur):
        joueur.afficher_score()
          
        self.afficher_le_plateau()
        print(f'\nTu as maintenant {len(joueur.score)} camemberts ! \n')
        print(" ".join(joueur.score))
        input('\nAppuie sur Entrée pour finir le tour !\n')


    def fin_de_partie(self, joueur):
        
        for joueur in self.joueurs:
            if len(joueur.score) == 6:
                print(f'--------------------------\n\n👑 {joueur.nom_du_joueur} : {" ".join(joueur.score)}\n')
            else:
                print(f'--------------------------\n\n💩 {joueur.nom_du_joueur} 💩 : {" ".join(joueur.score)}\n')
            print(f'Tu as répondu correctement à {len(joueur.tot_bonnes_reponses)} sur {len(joueur.tot_reponses_repondues)} questions !\n')

            for categorie in joueur.score and self.categories:
                print(f'{categorie} : {joueur.tot_bonnes_reponses.count(categorie)} / {joueur.tot_reponses_repondues.count(categorie)} {int(joueur.tot_reponses_repondues.count(categorie) and joueur.tot_bonnes_reponses.count(categorie)/joueur.tot_reponses_repondues.count(categorie)*100 or 0)}%\n\n')

        
    
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
        os.system('clear')
        self.fin_de_partie(joueur)
                                
