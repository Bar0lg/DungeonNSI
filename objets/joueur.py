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
        self.explvl = 1                             #Niveau du personnage
        self.exp = 0                                #Experiance du personnage
        self.expcap = 10                            #Experiance que le joueur doit atteindre pour augemanter de niveau

    def isDead(self):                               #Vérifie si le joueur est mort
        if self.pv <= 0:
            return True
        return False


    def montreStats(self):
        """
            Ce script affiche les stats du personnage
            Ce script ne retourne aucune valeur
        """
        print("""---%s--------------\nvie:%s/%s for:%s mana:%s/%s def:%s vit:%s exp:%s/%s"""%(self.nom,self.pv,self.pvmax,self.force,self.mana,self.manamax,self.defence,self.vitesse,self.exp,self.expcap))
        input()
        return None

    def EquipArme(self,arme):
        """
            Ce script demande si le joueur veut equiper une nouvelle arme
            une arme a un effet sur la force et le mana maximum
            Dans le jeu c'est un processus irrevesible
            Ce script ne retourne aucune valeur
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
            Ce script ne retourne aucune valeur
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


    def Ajoutexp(self,exp_gagne):
        """
            Ce script ajoute de l'experiance au personnage
            et si'il depasse le cap d'experiance ce script lr fait monter au niveau superieur
            quand le joueur augemente de niveau il gagne entre 1 et 5 points dans chaque stats
            et le prochain cap est 2.5 fois plus grand que le précédent
            Ce script ne retourne aucune valeur
        """
        print("Vous avez gagne %s exp"%(exp_gagne))
        input()
        self.exp += exp_gagne
        if self.exp >= self.expcap: #Si l'xp du joueur est asser haute pour monter de niveau
            print("Vous monter de niveau")
            self.pv    += random.randint(1,5)
            self.force  += random.randint(1,5)
            self.manamax+= random.randint(1,5)
            self.defence+= random.randint(1,5)
            self.vitesse+= random.randint(1,5)
            self.explvl += 1 #Le joueur gagne un Niveau
            self.expcap = self.expcap * 2.5 #On met en place le prochain cap d'Experiance
            input()
            return None


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
