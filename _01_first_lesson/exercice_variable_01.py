#Demander le nom de l'utilisateur et prenom et le stocker dans une variable
#Demander le prenom de l'utilisateur  et le stocker dans une variable
#Demander un premier chiffre a l'utilisateur et le stocker dans une variable
#Demander un second chiffre a l'utilisateur et le stocker dans une variable
#Afficher la phrase "Bonjour {nom} {prenom} vos chiffres sont {chiffre_a} et {chiffre_b}"
#Afficher la phrase " Le resultat de l'addition des chiffres est egale a {addidtion}"
#Afficher la phrase " Le resultat de la soustraction des chiffres est egale a {soustraction}"
#Afficher la phrase " Le resultat de la multiplication des chiffres est egale a {multiplication}"
#Afficher la phrase " Le resultat de la division des chiffres est egale a {division}"

## Les donnees entoures de {} sont des variables tu peux utiliser ces noms de variables la au total tu auras besoin de 8 variables
## Afficher fait reference a la fonction print() tu devras donc utiliser print 5 fois
## Pour recuperer des donnees d'un utilisateur on utilise la fonction input() et on oublie pas de mettre les resultats dans une variable (regarde ce qu'on avait fait lundi) donc 4 input() au total

from __future__ import division


nom = input("Quel est votre nom : ")
prenom = input("Quel est votre preom : ")
chiffre_a = int(input("Quel est votre premier chiffre : "))
chiffre_b = int(input("Quel est votre second chiffre : "))
somme = chiffre_a + chiffre_b
soustraction = chiffre_a - chiffre_b
multiplication = chiffre_a * chiffre_b
division = chiffre_a / chiffre_b

print("Bonjour " + nom + " " + prenom + " vos chiffres sont " + str(chiffre_a) + " et " + str(chiffre_b))
print("Le resultat de l'addition des chiffres est egale a " + str(somme))
print("Le resultat de la soustraction des chiffres est egale a " + str(soustraction))
print("Le resultat de la multiplication des chiffres est egale a " + str(multiplication))
print("Le resultat de la division des chiffres est egale a " + str(division))