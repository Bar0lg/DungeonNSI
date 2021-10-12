#Comme le code du jouer et du monstre est tres similaire je commanterais que
#se qui change par rapport a l'objet Joueur

import random
import copy


class monstre:

    def __init__(self,nom,description,levelmin,levelmax,vie,force,defence,vitesse,exp):
        self.nom = nom
        self.description = description  #description du monstre
        self.levelmin = levelmin        #Niveau minimum ou le monstre peut etre trouvé
        self.levelmax = levelmax        #Niveau maxmum ou le monstre peut etre trouvé
        self.pvmax = vie
        self.pv = vie
        self.force = force
        self.defence = defence
        self.vitesse = vitesse
        self.exp = exp                  #Experience donnée au joueur quand le mostre meurt

    def isDead(self):
        if self.pv <= 0:
            return True
        return False




def generer_liste_monstre():
    Dummy = monstre("Dummy","Un mostre Test",1,5,100,20,35,10,10)

    return [Dummy]
