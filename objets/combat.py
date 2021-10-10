"""
    Ce ficher contient tout se qui conserne les combats nottament:

    L'objet Combat gere tt les changements de stats et calculs
    La fonction Combat gere l'interface de combat renvoie True en cas de victoire
    et False en cas de defaite
"""

import random
import copy


class Combat_Class:

    def Fuite(self,Joueur,monstre):
        """
            Ce script calcul les chances de fuite du Joueur
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




def combat_Fontion(Joueur,monstre):
    Combat = Combat_Class()
    print("Vous affronter un %s \n" % (monstre.nom))  #Affiche nom
    print(monstre.description + "\n")                          #Et description du monstre

    while True:#Boucle de combat
        #Verifie si l'un des 2 est mort
        if Joueur.isDead() == True:
            return False
        elif monstre.isDead()==True:
            return True

        else:
            #Demande au joueur ce qu'il veut faire
            print("Que voulez vous faire \n\n0)Voir les stats\n1)Attaquer\n2)Special\n3)Objet\n4)Fuite")
            choix_joueur_combat = str(input())

            if choix_joueur_combat == "0":  #affiche les stats du jour et du monstre
                print("""---%s--------------
vie:%s for:%s mana:%s def:%s vit:%s"""%(Joueur.nom,Joueur.pv,Joueur.force,Joueur.mana,Joueur.defence,Joueur.vitesse,))
                print("""---%s--------------
vie:%s for:%s def:%s vit:%s"""%(monstre.nom,monstre.pv,monstre.force,monstre.defence,monstre.vitesse,))
                input()




            elif choix_joueur_combat == "1":
                print("Att")




            elif choix_joueur_combat == "2":
                print("spe")




            elif choix_joueur_combat == "3":
                print("Item")




            elif choix_joueur_combat == "4":
                if Combat.Fuite(Joueur,monstre) == True:
                    print("Vous reussier a vous enfuir")
                    return True #Le combat se finit
                else:
                    print("Vous echouer a vous enfuir")






            else:
                print("Veuller choisir un numero(0,1,2,3,4)")
