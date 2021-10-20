#Comme le code du joueur et du monstre est tres similaire je commenterais que
#ce qui change par rapport a l'objet Joueur

import random
import copy
import time

class monstre:

    def __init__(self,nom,description,levelmin,levelmax,vie,force,defence,vitesse,exp):
        self.nom = nom
        self.description = description  #description du monstre
        self.levelmin = levelmin        #Niveau minimum où le monstre peut etre trouvé
        self.levelmax = levelmax        #Niveau maximum où le monstre peut etre trouvé
        self.pvmax = vie
        self.pv = vie
        self.force = force
        self.defence = defence
        self.vitesse = vitesse
        self.exp = exp                  #Experience donnée au joueur quand le monstre meurt

    def isDead(self):
        if self.pv <= 0:
            return True
        return False




def generer_liste_monstre():
    Dummy = monstre("Dummy","Un monstre Test",1,5,20,20,35,10,10)


    return [Dummy]

def choisir_Monstre_Aleatoire(liste_monstre,PROFONDEUR):
    """
        Ce script choisit un monstre aléatoire de la liste et verifie s'il
        correspond a la profondeur actuelle
        Si oui le script retourne le monstre
        Si non le script rechoisit un monstre
    """
    while True:
        monstre = random.choice(liste_monstre)
        if (monstre.levelmin <= PROFONDEUR) and (monstre.levelmax >= PROFONDEUR):
            return monstre
        else:
            continue
