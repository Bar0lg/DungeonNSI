import random
import copy

class Joueur:

    def __init__(self,nom,vie,mana,force,defence,vitesse,inventaire,invspecial,arme,armure):
        self.nom = nom
        self.pvmax = vie                            #Vie maximale du personnage
        self.pv = vie                               #Vie du personnage
        self.manamax = mana         + arme.modmana  #Energie max pour les actions spécales
        self.mana = mana                            #Energie pour les actions spécales
        self.force = force          + arme.modforce #Impacte les dégats
        self.defence = defence      + armure.moddef #Impacte le nb de degats recus
        self.vitesse = vitesse      + armure.modvit #Impacte l'esquive + l'ordre des tours
        self.Inv = inventaire                       #L'inventaire du joueur
        self.inv_spe = invspecial                   #Iventaire pour les actions spéciales
        self.arme = arme                            #L'arme du joueur
        self.armure = armure                        #L'armure du joueur

    def isDead(self):                               #Vérifie si le joueur est mort
        if self.pv <= 0:
            return True
        return False


    def montreStats(self):
        """
            Ce script affiche les stats du personnage
        """
        print("""---%s--------------\nvie:%s/%s for:%s mana:%s/%s def:%s vit:%s"""%(self.nom,self.pv,self.pvmax,self.force,self.mana,self.manamax,self.defence,self.vitesse,))


    def EquipArme(self,arme):
        """
            Ce script demande si le joueur veut equiper une nouvelle arme
            une arme a un effet sur la force et le mana maximum
            Dans le jeu c'est un processus irrevesible
        """
        print("Vous trouver %s \n\n %s"%(arme.nom,arme.description))
        print("Voulez vous l'equiper a la place de %s?[O/N]"%(self.arme.nom))
        print("Force:%s --> %s"%(self.force,(self.force - self.arme.modforce) + arme.modforce))#Montre comment se manifeste le changement
        print("Mana:%s -->%s"%(self.manamax,(self.manamax - self.arme.modmana) + arme.modmana))
        while True: #Boucle jusqua ce que le joueur aie fait une désision
            choix_joueur = input(">")
            if choix_joueur.upper() == "O":
                self.force -= self.arme.modforce    #Retire les modifications de l'ancienne arme
                self.manamax -= self.arme.modmana
                self.force += arme.modforce    #Applique les modifications de la nouvelle arme
                self.manamax += arme.modmana
                self.arme = arme
                return None

            elif choix_joueur.upper() == "N":
                print("Vous choisisser de ne pas equiper %s"%(arme.nom))
                return None
            else:
                print("Veuiller ecrire un choix valable (O,N)")

    def EquipArmure(self,armure):
        """
            C'est basiquement le meme script que EquipArme mais pour les armures
            Les armures affectent La defence et la vitesse
        """
        print("Vous trouver %s \n\n %s"%(armure.nom,armure.description))
        print("Voulez vous l'equiper a la place de %s?[O/N]"%(self.armure.nom))
        print("Defence:%s --> %s"%(self.defence,(self.defence - self.armure.moddef) + armure.moddef))#Montre comment se manifeste le changement
        print("Vittesse:%s -->%s"%(self.vitesse,(self.vitesse - self.armure.modvit) + armure.modvit))
        while True: #Boucle jusqua ce que le joueur aie fait une désision
            choix_joueur = input(">")
            if choix_joueur.upper() == "O":
                self.defence -= self.armure.moddef    #Retire les modifications de l'ancienne armure
                self.vitesse -= self.armure.modvit
                self.defence += armure.moddef           #Applique les modifications de la nouvelle arme
                self.vitesse += armure.modvit
                self.armure = armure
                return None

            elif choix_joueur.upper() == "N":
                print("Vous choisisser de ne pas equiper %s"%(arme.nom))
                return None
            else:
                print("Veuiller ecrire un choix valable (O,N)")
















def assigner_classe(classe,nom,liste_armes,liste_armures):
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

        arme = liste_armes[0],
        armure = liste_armures[0])
