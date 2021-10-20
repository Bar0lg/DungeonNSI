"""
    Ce code crée les armes et armures
    Les armes modifient la force et la mana
    les armures modifient la défance et vitesse
    gen_list_arme() génère tt les armes
    gen_list_armures() génère tt les armures

"""

class Arme:
    def __init__(self,nom,description,modforce,modmana):
        self.classe = "Arme"
        self.nom = nom
        self.description = description
        self.modforce = modforce        #Modification apportée à la force du personnage
        self.modmana = modmana          #Modification apportée à la mana du personnage

class Armure:
    def __init__(self,nom,description,moddef,modvit):
        self.classe = "Armure"
        self.nom = nom
        self.description = description
        self.moddef = moddef            #Modification apportée à la defence du personnage
        self.modvit = modvit            #Modification apportée à la vittesse du personnage


def gen_list_arme(): #Genere les armes et les mets dans une liste
    Dague = Arme("Dague","Une petite dague",3,-1)
    OP = Arme("OP","L'arme des devs", 50,3)
    return [Dague,OP]



def gen_list_armures():
        Cuir = Armure("Armure en cuir","C'est une armure en cuir usée",5,0)
        Platine = Armure("Armure de Platine","C'est une magnifique armure faite de Platine",20,-10)
        return [Cuir,Platine]
