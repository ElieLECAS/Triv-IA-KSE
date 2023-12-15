from random import randint
class le_de:

    def __init__(self):
        self.resultat = self.lance_de()

    def lance_de(self):
        resultat = randint(1,6)
        return resultat
       

    def affiche_le_resultat(self):
        r=self.resultat
        print(r)

de1=le_de()
de1.lance_de()
de1.affiche_le_resultat()
#  verifier comment est parcouru le code à travers les méthodes