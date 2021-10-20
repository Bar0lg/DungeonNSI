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
    Mannequin   = monstre("Mannequin","Un Mannequin animé",1,1,10,20,35,10,8)
    Bat         = monstre("Chauve souris","Une petite Chauve souris,",1,1,7,30,30,50,15)
    Kobold      = monstre("Kobold","Un lézard humanoid",1,1,15,20,30,30,10)
    Squelette   = monstre("Squelette","Un squelette animé par la magie",1,2,3,35,2,2,1)
    Araignée_P  = monstre("Petite Araignée","Une petite araignée",1,2,20,30,12,20,15)
    Slime       = monstre("Slime","Une boule de gelée verte",1,2,15,30,20,5,12)
    Orc         = monstre("Orc","Un orc des montagnes",2,3,20,60,30,20,30)
    Nain        = monstre("Nain","Un nain des montagnes",2,3,20,20,60,20,20)
    Fantome     = monstre("Fantome","Une âme hantée",2,3,25,80,40,70,30)
    Araignée_G  = monstre("Grande araignée","Une araignée géante",3,4,30,80,45,90,60)
    Liche       = monstre("Liche","Une puissante liche utilisant le pouvoir des morts pour attaquer",3,4,50,60,40,100,50)
    Mimic       = monstre("Mimic","Une créature imitant les objets au alentours",3,4,40,100,60,100,35)
    Abomination = monstre("Abomination","Une abomination sortie des enfers",4,4,50,100,80,42,40)
    Terreur     = monstre("Terreur","Une horreur insescriptible",4,4,35,100,150,35,70)
    Mort        = monstre("La mort","La mort elle même",4,4,40,300,40,60,65)
    #Ce monstre est le boss de fin de jeu
    #On peut pas le rencontrer normallment
    #Il est assigné a la variable BOSS au debut de main.py
    Roi_Squelette = monstre("Le roi squelette","Gardien de l'amulette de Yendor, son œil bleu menacant illumine les tenèbres!",-1,-1,100,80,80,300,0)

    return [Mannequin,Bat,Kobold,Squelette,Araignée_P,Slime,Orc,Nain,Fantome,Araignée_G,Liche,Mimic,Abomination,Terreur,Mort,Roi_Squelette]

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
