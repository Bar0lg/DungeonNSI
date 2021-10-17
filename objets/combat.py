"""
    Ce ficher contient tout se qui conserne les combats nottament:

    L'objet Combat gere tt les changements de stats et calculs
    La fonction Combat gere l'interface de combat renvoie True en cas de victoire
    et False en cas de defaite
"""

import random
import copy


class Combat_Class:

    def Attack(self,Attaquant,defenceur):
        """
            L'algoritme de combat se fait comme sa: Degats = Attaque/Defance + Attaque*random(0.1 et 0.4)
        """
        Degats = round(Attaquant.force /defenceur.defence + Attaquant.force * random.uniform(0.1,0.3))
        print("%s attaque %s infligant %s degats!!"%(Attaquant.nom,defenceur.nom,Degats))
        defenceur.pv -= Degats
        input()
        return None


    def Fuite(self,Joueur,monstre):
        """
            Ce script calcule les chances de fuite du Joueur
            Pour cela j'utilise le meme algoritme de fuite que les jeux pokemon
            de 3eme et 4 eme generation (https://bulbapedia.bulbagarden.net/wiki/Escape)
            Renvoie True en cas de reussite et False en cas de defaite
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
            Celuit qui attaque en premier est celuit qui as le plus de vitesse des deux
            S'il ont la meme vitesse c'est aléatoire
            Retourne 0 si le joueur commance
            Retourne 1 si le monstre commance
        """
        if Joueur.vitesse > monstre.vitesse:
            return 0
        elif Joueur.vitesse < monstre.vitesse:
            return 1
        else:
            return random.randint(0,1)


def combat_Fontion(Joueur,monstre_modele):
    monstre = copy.deepcopy(monstre_modele) #Cree une copie du modèle du monstre
    Combat = Combat_Class()
    print("Vous affronter un %s \n" % (monstre.nom))  #Affiche nom
    print(monstre.description + "\n")                          #Et description du monstre

    while True:#Boucle de combat
        #Verifie si l'un des 2 est mort
        if Joueur.isDead() == True:
            print("Vous mourrez")
            input()
            return False
        elif monstre.isDead()==True:
            print("%s meurt"%(monstre.nom))
            Joueur.Ajoutexp(monstre.exp)    #Donne au joueur de l'exp pour avoir tué le monstre
            return True

        else:
            #Demande au joueur ce qu'il veut faire
            print("Que voulez vous faire \n\n0)Voir les stats\n1)Attaquer\n2)Special\n3)Fuite")
            choix_joueur_combat = str(input(">"))

            if choix_joueur_combat == "0":  #Affiche les stats du jour et du monstre
                print("""---%s--------------\nvie:%s/%s for:%s mana:%s/%s def:%s vit:%s"""%(Joueur.nom,Joueur.pv,Joueur.pvmax,Joueur.force,Joueur.mana,Joueur.manamax,Joueur.defence,Joueur.vitesse,))
                print("""---%s--------------\nvie:%s/%s for:%s def:%s vit:%s"""%(monstre.nom,monstre.pv,monstre.pvmax,monstre.force,monstre.defence,monstre.vitesse,))
                input()




            elif choix_joueur_combat == "1":
                ordre = Combat.quiAttaquePremier(Joueur,monstre) #Detemine l'ordre
                if ordre == 0:
                    Combat.Attack(Joueur,monstre)   #Attaque du joueur
                    Combat.Attack(monstre,Joueur)   #Attaque du monstre
                else:
                    Combat.Attack(monstre,Joueur)   #Attaque du monstre
                    Combat.Attack(Joueur,monstre)   #Attaque du joueur




            elif choix_joueur_combat == "2":
                print("spe")




            elif choix_joueur_combat == "3":
                if Combat.Fuite(Joueur,monstre) == True:
                    print("Vous reussier a vous enfuir")
                    return True #Le combat se finit
                else:
                    print("Vous echouer a vous enfuir")
                    Combat.Attack(monstre,Joueur)






            else:
                print("Veuller choisir un numero(0,1,2,3)")
