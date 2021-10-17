#Code crée par Tristan Lemoine, Damien Tremerie, Tony Nguyen

#Projet de jeu video pour la NSI

#Ceci est le fichier qu'on lance pour lancer le jeu

import random
import copy #Cette librairie a la commade deepcopy() qui me permet de faire une vraie copie d'un objet se qui me permaettra de modifier la copie sans affecter l'original


from objets.joueur import *         #Importe l'objet du Joueur + commande assigner_classe
from objets.monstres import *       #Importe mporte l'objet du Joueur + commande generer_liste_monstre
from objets.combat import *         #Importe Tout ce qui est lié au combat
from objets.armes_armures import *  #Importe les armes et armures


PROFONDEUR = 4
Niv_par_pronfondeur = 5


def main():         #Fonction Principale
    Monstres = generer_liste_monstre()
    liste_armes = gen_list_arme()
    liste_armures = gen_list_armures()
    print("Bienvenue dans DongeonNSI \n\n")
    print("Appyer sur Entree pour continuer")
    input()
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

    for i in range(1,PROFONDEUR):
        print("Vous entrez dans le niveau %s"%(i))
        input()
        for k in range(Niv_par_pronfondeur):
            print("Vous entrez dans une salle...")
            input()
            monstre_a_affronter = choisir_Monstre_Aleatoire(Monstres,i)
            print("Un %s apparait"%(monstre_a_affronter.nom))
            res_combat = combat_Fontion(Player,monstre_a_affronter)


            if res_combat == False: #Si le joueur meurt
                print("Vous n'avez pas réussit a trouver l'ammulette")
                return None #Fait sortir du jeu

            print("Vous entrez dans une salle...")
            input()
            print("Deux objets s'offrent a vous mais vous en pouvez en prendre qu'un:")
            obj1 = random.choice(liste_armes+liste_armures)
            obj2 = random.choice(liste_armes+liste_armures)
            print("1)%s \n\n2)%s"%(obj1.nom,obj2.nom))
            while True:
                choix_joueur = input(">")
                if choix_joueur == "1":
                    pass
                elif choix_joueur == "2":
                    pass
                else:
                    print("Veuiller entrer un numero valide(1,2)")
        print("Vous trouver un escalier pour le niveau %s \n Appuyer sur entrer"%(i+1))
        input()




if __name__ == "__main__":
    main()
