#Code crée par Tristan Lemoine, Damien Tremerie, Tony Nguyen

#Projet de jeu video pour la NSI

#Ceci est le fichier qu'on lance pour lancer le jeu

import random
import copy #Cette librairie a la commade deepcopy() qui me permet de faire une vraie copie d'un objet ce qui me permaettra de modifier la copie sans affecter l'original
import time

from objets.joueur import *         #Importe l'objet du Joueur + commande assigner_classe
from objets.monstres import *       #Importe l'objet du Joueur + commande generer_liste_monstre
from objets.combat import *         #Importe tout ce qui est lié au combat
from objets.armes_armures import *  #Importe les armes et armures


NIVEAU = 5                  #Definit le nombre de Niveau dans le jeu
COMBAT_PAR_NIVEAU = 3       #Definit le nombre de combat dans un niveau


def main():         #Fonction Principale
    Monstres = generer_liste_monstre()
    liste_armes = gen_list_arme()
    liste_armures = gen_list_armures()
    BOSS = Monstres[0]  #Definit quel monstre est le boss final du jeu
    print("Bienvenue dans Dungeon \n\n")
    time.sleep(2)
    print("Veuillez choisir votre classe \n\n1)Guerrier\n\n2)Mage\n\n3)Archer")

    while True:#Boucle jusqua ce que le joueur prend une classe
        choix_joueur = input(">")

        if choix_joueur == "1":
            nom = str(input("Quel est votre nom:"))
            Player = assigner_classe("Guerrier",nom,liste_armes,liste_armures) #Crée le Joueur
            break       #Brise la boucle
        elif choix_joueur == "2":
            nom = str(input("Quel est votre nom:"))
            Player = assigner_classe("Mage",nom,liste_armes,liste_armures) #Crée le Joueur
            break
        elif choix_joueur == "3":
            nom = str(input("Quel est votre nom:"))
            Player = assigner_classe("Archer",nom,liste_armes,liste_armures) #Crée le Joueur
            break
        else:
            print("Veuiller entrer un numero valide(1,2,3)")

    print("Vous entrez dans le donjon de la mort à la recherche de l'amulette de Yendor")

    #Boucle principale

    for i in range(1,NIVEAU):
        print("Vous entrez dans le niveau %s"%(i))
        time.sleep(2)
        for k in range(COMBAT_PAR_NIVEAU):

            #Combat du Niveau

            print("Vous entrez dans une salle...")
            time.sleep(2)
            monstre_a_affronter = choisir_Monstre_Aleatoire(Monstres,i)
            print("Un %s apparait"%(monstre_a_affronter.nom))
            time.sleep(2)
            res_combat = combat_Fontion(Player,monstre_a_affronter)


            if res_combat == False: #Si le joueur meurt
                print("Vous n'avez pas réussit a trouver l'amulette")
                return None #Fait sortir du jeu


            #Recompence apres le combat

            print("Vous entrez dans une salle...")
            time.sleep(2)
            print("Deux objets s'offrent a vous mais vous ne pouvez qu'en prendre qu'un(Vous pouvez aussi vous reposez):")
            obj1 = random.choice(liste_armes+liste_armures)
            obj2 = random.choice(liste_armes+liste_armures)
            print("1)%s \n\n2)%s\n\n3)Vous reposez"%(obj1.nom,obj2.nom))


            while True:                         #Boucle de choix
                choix_joueur = input(">")
                if choix_joueur == "1":
                    if obj1.classe == "Arme":   #Si l'objet est une arme
                        Player.EquipArme(obj1)
                        break                   #Casse la boucle
                    else:                       #Si c'est une armure
                        Player.EquipArmure(obj1)
                        break                   #Casse la boucle
                elif choix_joueur == "2":
                    if obj2.classe == "Arme":   #Si l'objet est une arme
                        Player.EquipArme(obj2)
                        break                   #Casse la boucle
                    else:                       #Si c'est une armure
                        Player.EquipArmure(obj2)
                        break                   #Casse la boucle
                elif choix_joueur == "3":
                    #Redonne au joueur 30 vie et 50 mana
                    print("Vous prenez une pause...")
                    time.sleep(4)
                    Player.pv = min(Player.pv + 6,Player.pvmax)
                    Player.mana = min(Player.mana + 50 ,Player.manamax)
                    break #Casse la boucle
                else:
                    print("Veuillez entrer un numero valide(1,2,3)")
        print("Vous trouvez un escalier pour le niveau %s \n"%(i+1))
        time.sleep(2)


    #Dernier niveau ou le joueur affronte un boss
    print("Vous arrivez au dernier niveau...")
    time.sleep(2)
    print("L'amulette est a votre portée...")
    time.sleep(2)
    print("Mais il vous reste une derniere epreuve a affronter...\n\n\n")
    time.sleep(2)
    res_combat = combat_Fontion(Player,BOSS)    #Fait affronter le boss du jeu
    if res_combat == False: #Si le joueur meurt
        print("Vous n'avez pas réussit a trouver l'amulette")
        return None #Fait sortir du jeu

    #Message de fin de jeu
    time.sleep(5)
    print("\n\n\nApres un combat acharné..")
    time.sleep(2)
    print("Vous atteignez enfin l'amulette\n\n")
    time.sleep(2)
    print("Vous remontez à la surface et devenez riche!!!")
    time.sleep(2)
    print("\n\n\nMerci d'avoir joué")
    time.sleep(2)
    print("Un jeu de: \n\nTristan Lemoine \nDamien Tremerie \nTony Nguyen")
    return None #Fait sortir du jeu

if __name__ == "__main__":
    main()
