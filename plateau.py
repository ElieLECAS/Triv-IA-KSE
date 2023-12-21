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

        if self.grille[joueur.x] =='🟥':
            if joueur.difficulte == "Facile":
                params=('SQL','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('SQL','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('SQL','Difficle')
                print(self.access.read_questions(params))
            
        elif self.grille[joueur.x] =='🟨':
            if joueur.difficulte == "Facile":
                params=('Python','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('Python','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('Python','Difficle')
                print(self.access.read_questions(params))

        elif self.grille[joueur.x] =='🟩':
            if joueur.difficulte == "Facile":
                params=('Ligne de commande','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('Ligne de commande','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('Ligne de commande','Difficle')
                print(self.access.read_questions(params))

        elif self.grille[joueur.x] =='🟦':
            if joueur.difficulte == "Facile":
                params=('Actualités IA','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('Actualités IA','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('Actualités IA','Difficle')
                print(self.access.read_questions(params))

        elif self.grille[joueur.x] =='🟪':
            if joueur.difficulte == "Facile":
                params=('Git/Github','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('Git/Github','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('Git/Github','Difficle')
                print(self.access.read_questions(params))

        elif self.grille[joueur.x] =='🟫':
            if joueur.difficulte == "Facile":
                params=('Thème mystère','Facile')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Intermediaire":
                params=('Thème mystère','Intermediaire')
                print(self.access.read_questions(params))
            if joueur.difficulte == "Difficle":
                params=('Thème mystère','Difficle')
                print(self.access.read_questions(params))


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
        self.attribution_categorie(joueur)

    def questions_reponses(self, joueur):
        if input(f'\nQuestion de niveau {joueur.difficulte} \nParis est la capitale de la France.\na. True   b. False\n\nVotre réponse : \n') == "a":
            os.system('clear')
            print(f'Bravo ! {joueur.nom_du_joueur}\n')
            joueur.tot_bonnes_reponses.append(self.grille[joueur.x])
            if len(joueur.score) == 2:
                joueur.difficulte = "Intermediaire"
            elif len(joueur.score) == 4:
                joueur.difficulte = "Difficile"
        else:
            os.system('clear')
            print('Perdu ! \n')

        joueur.tot_reponses_repondues.append(self.grille[joueur.x])


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

        
            # print(f'''
            #       🟥 : {joueur.tot_bonnes_reponses.count("🟥")} / {joueur.tot_reponses_repondues.count("🟥")} {int(joueur.tot_reponses_repondues.count("🟥") and joueur.tot_bonnes_reponses.count("🟥")/joueur.tot_reponses_repondues.count("🟥")*100 or 0)}%\n

            #       🟨 : {joueur.tot_bonnes_reponses.count("🟨")} / {joueur.tot_reponses_repondues.count("🟨")} {int(joueur.tot_reponses_repondues.count("🟨") and joueur.tot_bonnes_reponses.count("🟨")/joueur.tot_reponses_repondues.count("🟨")*100 or 0)}%\n

            #       🟩 : {joueur.tot_bonnes_reponses.count("🟩")} / {joueur.tot_reponses_repondues.count("🟩")} {int(joueur.tot_reponses_repondues.count("🟩") and joueur.tot_bonnes_reponses.count("🟩")/joueur.tot_reponses_repondues.count("🟩")*100 or 0)}%\n

            #       🟦 : {joueur.tot_bonnes_reponses.count("🟦")} / {joueur.tot_reponses_repondues.count("🟦")} {int(joueur.tot_reponses_repondues.count("🟦") and joueur.tot_bonnes_reponses.count("🟦")/joueur.tot_reponses_repondues.count("🟦")*100 or 0)}%\n

            #       🟪 : {joueur.tot_bonnes_reponses.count("🟪")} / {joueur.tot_reponses_repondues.count("🟪")} {int(joueur.tot_reponses_repondues.count("🟪") and joueur.tot_bonnes_reponses.count("🟪")/joueur.tot_reponses_repondues.count("🟪")*100 or 0)}%\n

            #       🟫 : {joueur.tot_bonnes_reponses.count("🟫")} / {joueur.tot_reponses_repondues.count("🟫")} {int(joueur.tot_reponses_repondues.count("🟫") and joueur.tot_bonnes_reponses.count("🟫")/joueur.tot_reponses_repondues.count("🟫")*100 or 0)}%\n

                
            # ''')
    
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
                                
access = MySQLHandler(host='localhost' , user='kevin' , password='Plasma2020@' , database='trivia_db')   
plateau1 = Plateau(access)
plateau1.peupler_le_plateau(int(input("Combien de joueurs : ")))
plateau1.deroulement()