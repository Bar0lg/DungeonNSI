import random
import copy

class Joueur:

    def __init__(self,nom,vie,mana,force,defence,vitesse,inventaire,invspecial,arme,armure):
        self.nom = nom
        self.pvmax = vie            #Vie maximale du personnage
        self.pv = vie               #Vie du personnage
        self.manamax = mana         #Energie max pour les actions spécales
        self.mana = mana            #Energie pour les actions spécales
        self.force = force          #Impacte les dégats
        self.defence = defence      #Impacte le nb de degats recus
        self.vitesse = vitesse      #Impacte l'esquive + l'ordre des tours
        self.Inv = inventaire       #L'inventaire du joueur
        self.inv_spe = invspecial   #Iventaire pour les actions spéciales
        self.arme = arme            #L'arme du joueur
        self.armure = armure        #L'armure du joueur

    def isDead(self):               #Vérifie si le joueur est mort
        if self.pv <= 0:
            return True
        return False

def assigner_classe(classe,nom):
    if classe == "Guerrier":
        return Joueur(
        nom = nom,
        vie=100,
        mana=50,
        force = 50,
        defence=50,
        vitesse=50,
        inventaire=[

            ],
        invspecial = None,

        arme = None,
        armure = None)
