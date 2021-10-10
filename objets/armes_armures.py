"""
    Ce code crée les armes et armures
    Les armes modifient la force et la commanterais
    les armures modifient la defance et vitesse
"""

class Arme:
    def __init__(self,nom,description,modforce,modmana):
        self.nom = nom
        self.description = description
        self.modforce = modforce        #Modification apporté a la force du personnage
        self.modmana = modmana          #Modification apporté a la mana du personnage

class Armure:
    def __init__(self,nom,description,moddef,modvit):
        self.nom = nom
        self.description = description
        self.moddef = moddef            #Modification apporté a la defence du personnage
        self.modvit = modvit            #Modification apporté a la vittesse du personnage
