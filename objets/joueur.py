class Joueur:

    def __init__(self,nom,vie,mana,force,defence,vitesse,inventaire,invspecial):
        self.nom = nom
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

def assigner_classe(classe,nom):
    if classe == "Guerrier":
        return Joueur(
        nom = nom,
        vie=100,
        mana=100,
        force = 100,
        defence=100,
        vitesse=100,
        inventaire=[

            ],
        invspecial = None,
        )
