#Code crée par Tristan Lemoine, Damien Tremerie, Tony Nguyen

#Projet de jeu video pour la NSI

#Ceci est le fichier qu'on lance pour lancer le jeu

import random
import copy #Cette librairie a la commade deepcopy() qui me permet de faire une vraie copie d'un objet se qui me permaettra de modifier la copie sans affecter l'original
import time

from objets.joueur import *         #Importe l'objet du Joueur + commande assigner_classe
from objets.monstres import *       #Importe mporte l'objet du Joueur + commande generer_liste_monstre
from objets.combat import *         #Importe Tout ce qui est lié au combat
from objets.armes_armures import *  #Importe les armes et armures


NIVEAU = 0              #Definit le nb de Niveau dans le jeu
COMBAT_PAR_NIVEAU = 0     #Definit le nombre de combat dans un niveau


def main():         #Fonction Principale
    Monstres = generer_liste_monstre()
    liste_armes = gen_list_arme()
    liste_armures = gen_list_armures()
    BOSS = Monstres[0]  #Definit quel monstre est le boss final du jeu
    print("Bienvenue dans DongeonNSI \n\n")
    time.sleep(1)
    print("Veuiller choisir votre classe \n\n1)Guerrier")

    while True:#Boucle jusqua ce que le joueur prend une classe
        choix_joueur = input(">")

        if choix_joueur == "1":
            nom = str(input("Quel est votre nom:"))
            Player = assigner_classe("Guerrier",nom,liste_armes,liste_armures) #Crée le Joueur
            break       #Brise la boucle
        else:
            print("Veuiller entrer un numero valide(1)")

    print("Vous entrez dans le donjon de la mort a la recherche de l'amullete de Yandor")

    #Boucle principale

    for i in range(1,NIVEAU):
        print("Vous entrez dans le niveau %s"%(i))
        time.sleep(1)
        for k in range(COMBAT_PAR_NIVEAU):

            #Combat du Niveau

            print("Vous entrez dans une salle...")
            time.sleep(1)
            monstre_a_affronter = choisir_Monstre_Aleatoire(Monstres,i)
            print("Un %s apparait"%(monstre_a_affronter.nom))
            time.sleep(1)
            res_combat = combat_Fontion(Player,monstre_a_affronter)


            if res_combat == False: #Si le joueur meurt
                print("Vous n'avez pas réussit a trouver l'ammulette")
                return None #Fait sortir du jeu


            #Recompence apres le combat

            print("Vous entrez dans une salle...")
            time.sleep(1)
            print("Deux objets s'offrent a vous mais vous en pouvez en prendre qu'un:")
            obj1 = random.choice(liste_armes+liste_armures)
            obj2 = random.choice(liste_armes+liste_armures)
            print("1)%s \n\n2)%s"%(obj1.nom,obj2.nom))


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
                else:
                    print("Veuiller entrer un numero valide(1,2)")
        print("Vous trouver un escalier pour le niveau %s \n"%(i+1))
        time.sleep(1)


    #Dernier niveau ou le joueur affronte un boss
    print("Vous arriver au dernier niveau...")
    time.sleep(2)
    print("L'amulette est a votre portée...")
    time.sleep(2)
    print("Mais il vous reste une derniere epreuve a affronter...\n\n\n")
    time.sleep(2)
    res_combat = combat_Fontion(Player,BOSS)    #Fait affronter le boss du jeu
    if res_combat == False: #Si le joueur meurt
        print("Vous n'avez pas réussit a trouver l'ammulette")
        return None #Fait sortir du jeu

    #Message de fin de jeu
    time.sleep(5)
    print("\n\n\nApres un combat acharné..")
    time.sleep(1)
    print("Vous atteigner enfin l'amulette\n\n")
    time.sleep(1)
    print("Vous remontez a la surface et devenez riche!!!")
    time.sleep(1)
    print("\n\n\nMerci d'avoir joué")
    time.sleep(1)
    print("Un jeu de Tristan Lemoine Damien Tremerie Tony Nguyen")
    return None #Fait sortir du jeu

if __name__ == "__main__":
    main()
