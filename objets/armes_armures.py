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
    Dague       = Arme("Dague","Une petite dague",3,-1)
    Branche     = Arme("Branche","Une branche d'arbre",1,1)
    Baton       = Arme("Baton","Un petit baton de mage",-5,10)
    Epee        = Arme("Epée","Une épée en fer",10,-5)
    MSword      = Arme("Master Sword","Une épée légendaire",30,0)
    SBaton      = Arme("Super Baton","Un baton réservée pour les grands mages",-10,60)
    Arc         = Arme("Un arc","Un arc",5,5)
    Sarc        = Arme("Super Arc","Un Arc surpuissant",10,10)
    Caillou     = Arme("Un caillou","Ce caillou est en réalité une piere d'infinitée",50,120)
    return [Dague,Branche,Baton,Epee,MSword,SBaton,Arc,Sarc,Caillou]



def gen_list_armures():
        Cuir    = Armure("Armure en cuir","C'est une armure en cuir usée",5,0)
        Fer     = Armure("Armure en Fer","Une armure en fer",10,-5)
        Maille  = Armure("Cotte de maille","Une cote de maille",5,5)
        Platine = Armure("Armure de Platine","C'est une magnifique armure faite de Platine",20,-10)
        Cape    = Armure("Cape","Cape de légertée",0,15)
        Kevlar  = Armure("Gilet pare-balle","Sa va pas etre tres utile contre la magie...",-10,-10)
        Diamant = Armure("Armure en diamant","Techniquement incassable,Techniquement très lourd",30,-20)
        Costume = Armure("Costume","Un costume de flash!",-20,50)
        return [Cuir,Fer,Maille,Platine,Cape,Kevlar,Diamant,Costume]
