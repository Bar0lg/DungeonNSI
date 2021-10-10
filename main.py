#Code crée par Tristan Lemoine, Damien Tremerie, Tony Nguyen

#Projet de jeu video pour la NSI

#Ceci est le fichier qu'on lance pour lancer le jeu

import random
from objets.joueur import *     #Importe l'objet du Joueur + commande assigner_classe
from objets.monstres import *   #Importe mporte l'objet du Joueur + commande generer_liste_monstre

import copy #Cette librairie a la commade deepcopy() qui me permet de faire une vraie copie d'un objet se qui me permaettra de modifier la copie sans affecter l'original


def main():         #Fonction Principale
    Monstres = generer_liste_monstre()
    print("Bienvenue dans DongeonNSI \n\n")
    print("Appyer sur Entree pour continuer")
    print("Veuiller choisir votre classe \n\n1)Guerrier")

    while True:#Boucle jusqua ce que le joueur prend une classe
        choix_joueur = input()

        if choix_joueur == "1":
            nom = str(input("Quel est votre nom:"))
            Player = assigner_classe("Guerrier",nom) #Crée le Joueur
            break       #Brise la boucle
        else:
            print("Veuiller entrer un numero valide(1)")



    print(Monstres)
    input("Fin programme")








if __name__ == "__main__":
    main()
