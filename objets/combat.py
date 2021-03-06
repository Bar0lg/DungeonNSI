"""
    Ce ficher contient tout ce qui concerne les combats nottament:

    L'objet Combat gere tout les changements de stats et calculs
    La fonction Combat gère l'interface de combat, renvoie True en cas de victoire
    et False en cas de défaite
"""

import random
import copy
import time

class Combat_Class:

    def Attack(self,Attaquant,defenceur):
        """
            L'algoritme de combat se fait comme ça: Degats = Attaque/Defance + Attaque*random(0.05 et 0.1)
        """
        Degats = round(Attaquant.force /defenceur.defence + Attaquant.force * random.uniform(0.05,0.1))
        print("%s attaque %s infligeant %s dégats!!"%(Attaquant.nom,defenceur.nom,Degats))
        defenceur.pv -= Degats
        time.sleep(2)
        return None

    def Special(self,Joueur,monstre):
        """
            Special est une action unique a chaque classe
            Guerrier:Attaque en ayant une defence améliorée (Mais attaque en dernier)
            Mage:Attaque tres puissante (Mais attaque en dernier)
            Archer:Attaque sans que le monstre attaque derriere
            Chaque Special coute 30 mana
            Renvoie rien
        """
        if Joueur.mana < 30:    #Fait passer le tour si le joueur n'a pas assez de mana
            print("Vous echouez a lancer votre attaque speciale par manque d'energie")
            time.sleep(2)
            return None

        #Special du guerrier
        elif Joueur.classe == "Guerrier":
            print("Vous deployer votre bouclier!!!!")
            time.sleep(2)
            Joueur.defence *= 10    #Multiplie la defence du Joueur par 10
            self.Attack(monstre,Joueur)
            Joueur.defence //= 10    #Remet La defence du joueur a la normalle
            self.Attack(Joueur,monstre)
            Joueur.mana -= 30       #Reduit la mana du joueur de 30
            return None

        #Special du Mage
        elif Joueur.classe == "Mage":
            self.Attack(monstre,Joueur)
            print("Vous invoquez une boule de feu!!!")
            time.sleep(2)
            Joueur.force *= 5      #Multiplie la force du Joueur par 5
            self.Attack(Joueur,monstre)
            Joueur.force //= 5    #Remet la force du joueur a la normale
            Joueur.mana -= 30       #Reduit la mana du joueur de 30
            return None

        #Special du Mage
        elif Joueur.classe == "Archer":
            print("Avant même que l'ennemi réagisse vous lui infligez une attaque éclair!!!")
            time.sleep(2)
            self.Attack(Joueur,monstre)
            Joueur.mana -= 30       #Reduit la mana du joueur de 30
            return None

    def Fuite(self,Joueur,monstre):
        """
            Ce script calcule les chances de fuite du Joueur
            Pour cela j'utilise le même algoritme de fuite que les jeux pokemon
            de 3eme et 4 eme generation (https://bulbapedia.bulbagarden.net/wiki/Escape)
            Renvoie True en cas de reussite et False en cas de défaite
        """
        if Joueur.vitesse >= monstre.vitesse:
            return True
        else:
            chances = ((Joueur.vitesse * 128)/monstre.vitesse)+30
            rand_num = random.randint(1,255)
            if rand_num <= chances:
                return True
            else:
                return False

    def quiAttaquePremier(self,Joueur,monstre):
        """
            Celui qui attaque en premier est celui qui a le plus de vitesse des deux
            S'ils ont la même vitesse c'est aléatoire
            Retourne 0 si le joueur commence
            Retourne 1 si le monstre commence
        """
        if Joueur.vitesse > monstre.vitesse:
            return 0
        elif Joueur.vitesse < monstre.vitesse:
            return 1
        else:
            return random.randint(0,1)


def combat_Fontion(Joueur,monstre_modele):
    monstre = copy.deepcopy(monstre_modele) #Creée une copie du modèle du monstre
    Combat = Combat_Class()
    print("Vous affrontez un %s \n" % (monstre.nom))  #Affiche nom
    print(monstre.description + "\n")                 #Et description du monstre

    while True:#Boucle de combat
        #Verifie si l'un des 2 est mort
        if Joueur.isDead() == True:
            print("Vous mourrez")
            time.sleep(2)
            return False
        elif monstre.isDead()==True:
            print("%s meurt"%(monstre.nom))
            Joueur.Ajoutexp(monstre.exp)    #Donne au joueur de l'exp pour avoir tué le monstre
            Joueur.pv = min(Joueur.pv + 10,Joueur.pvmax)        #Redonne 10 pv au joueur et 20 mana
            Joueur.mana = min(Joueur.mana + 20 ,Joueur.manamax)
            return True

        else:
            #Demande au joueur ce qu'il veut faire
            print("Que voulez vous faire \n\n0)Voir les stats\n1)Attaquer\n2)Special\n3)Fuite")
            choix_joueur_combat = str(input(">"))

            if choix_joueur_combat == "0":  #Affiche les stats du jour et du monstre
                print("""---%s--------------\nvie:%s/%s for:%s mana:%s/%s def:%s vit:%s"""%(Joueur.nom,Joueur.pv,Joueur.pvmax,Joueur.force,Joueur.mana,Joueur.manamax,Joueur.defence,Joueur.vitesse,))
                print("""---%s--------------\nvie:%s/%s for:%s def:%s vit:%s"""%(monstre.nom,monstre.pv,monstre.pvmax,monstre.force,monstre.defence,monstre.vitesse,))
                time.sleep(2)




            elif choix_joueur_combat == "1":
                ordre = Combat.quiAttaquePremier(Joueur,monstre) #Détemine l'ordre
                if ordre == 0:
                    Combat.Attack(Joueur,monstre)   #Attaque du joueur
                    Combat.Attack(monstre,Joueur)   #Attaque du monstre
                else:
                    Combat.Attack(monstre,Joueur)   #Attaque du monstre
                    Combat.Attack(Joueur,monstre)   #Attaque du joueur

            elif choix_joueur_combat == "2":    #Lance l'attaque speciale du joueur
                Combat.Special(Joueur,monstre)

            elif choix_joueur_combat == "3":
                if Combat.Fuite(Joueur,monstre) == True:
                    print("Vous réussissez a vous enfuir")
                    return True #Le combat se finit
                else:
                    print("Vous echouez a vous enfuir")
                    Combat.Attack(monstre,Joueur)

            else:
                print("Veullez choisir un numero(0,1,2,3)")
