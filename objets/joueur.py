class Joueur:

    def __init__(self,vie,mana,force,defence,vitesse,inventaire,invspecial):
        self.pv = vie               #Vie du personnage
        self.mana = mana            #Energie pour les actions spécales
        self.force = force          #Impacte les dégats
        self.defence = defence      #Impacte le nb de degats recus
        self.vitesse = vitesse      #Impacte l'esquive + l'ordre des tours
        self.Inv = inventaire       #L'inventaire du joueur
        self.inv_spe = invspecial   #Iventaire pour les actions spéciales

    def isDead(self):               #Vérifie si le joueur est mort
        if self.pv <= 0:
            return True
        return False

def assigner_classe(classe):
    if classe == "Guerrier":
        return Joueur(
        vie=200
        mana=75
        force = 150
        defence=120
        vitesse=50
        inventaire=[

            ]
        invspecial = None
        )
