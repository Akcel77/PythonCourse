# # 1 - demander à l'utilisateur de saisir son nom
# name = input("Saisir votre nom : ")
# print("Bienvenue : " , name)

# # 2 - demander à l'utilisateur de saisir les valeurs de a et de b
a = input("Tapez la valeur du nombre a : ")
b = input("Tapez la valeur du nombre b : ")
# Convertir les chaines de caractères en entier
a = int(a)
b = int(b)
s = a+b
print("La somme de a et de b est a + b = " , s)

# # 3 - lire les valeurs de a et b
# a = int(input("Tapez la valeur du nombre a : "))
# b = int(input("Tapez la valeur du nombre b : "))

# # Faire un test de comparaison pour trouver le plus grand 
# if (a > b):
#     print("Le maximum  de a et de b est : a = ", a)
# else:
#     print("Le maximum  de a et de b est : b = ", b)

# # 4 - # parcourir les 100 premiers nombres à l'aide de la boucle for
# for i in range(0,101):
#     print(i)

print(('   -     ') * 8)
# # 5 - # Lire la valeur de n
# n = input("Type value of the integer n : ")

# # Convertir n en entier
# n = int(n)
# # Tester si n est pair ou non
# if(n%2 == 0):
#     print("Le nombre '", n, "' tapé est pair ")
# else:
#     print("Le nombre '", n, "' tapé est impair ")


# # 6 - Demander à l'utilisateur de taper son âge 
# age = int(input("Tapez votre age : "))
# if(age > 18):
#     print("Vous êtes majeur !")
# else:
#     print("Vous êtes mineur !")


# # 7 - # Demander à l'utilisateur de taper 3 nombres  a, b, c
# a = int(input("Type a value of the number a "))
# b = int(input("Type a value of the number b "))
# c = int(input("Type a value of the number c "))

# # définir et initialiser le maximum à zero
# max = 0
# if(a > b and a > c):
#     max = a
# elif(b > c and b > a): 
#     max = b
# elif(c > a and c > b):
#     max = c
# else: 
#     max = max
# print("Le maximum des trois nombre est : max(a,b,c) = ", max)

# # 8 - Demander à l'utilisateur de saisir la valeur de l'entier n
# n = int(input("Type a value of the integer n "))

# # define et initialiser une variable auxiliaire j
# j = 0
# for i in range(1,n+1):
#     j = j + i 
# print("La somme  1 + 2 + 3 + ...+ ",n," = : ", j)


# # - 9 Demander à l'utilisateur de saisir la valeur de l'entier n
# n = int(input("Type a value of the integer n "))

# # define et initialiser une variable auxiliaire j
# j = 1
# for i in range(1,n+1):
#     j = j*i 
# print("Factorielle de n est : ",n,"! = : ", j)

# # 10 - importer le nombre pi à partir de la bibliothèque math
# from math import pi
# # lire la valeur du rayon r
# r = int(input("Saisissez la valeur du rayon r: "))
# # calcul du périmètre du cercle
# P = 2*pi*r
# # calcul de la surface du cercle
# S = pi*(r**2)
# print("Le périmètre du cercle de rayons r =",r," est P = ", P)  
# print("La surface du cercle de rayons r =",r," est S = ", S)


# # 11 - Recuperer la valeur de l'entier
# n = int(input("Tapez la valeur de l'entier n "))
# # parcourir tous les entiers inféreir ou égale à n
# for i in range(1,n+1):
#     # tester si i est un diviseur de n
#     if(n%i==0):
#         print("Le nombre ",i," est un diviseur de  ",n)


# # 12 - Partie 1
# # Lire la valeur de l'entier n
# n = int(input("Tapez la valeur de n "))
# print("La table de multiplication de : ", n," est :")
# for i in range(1,10):
#     print(i , " x ", n, " = ",i*n)
# # 12 - Partie 2
# for n in range(1,10):
#     #insert separator
#     print("--------------------------------------")
#     print("la table de multiplication de  : ", n," est :")
#     for i in range(1,10):
#         print(i , " x ", n, " = ",i*n)


# # 13 - Lire les valeurs de  a et  b
# a = int(input("Tapez la valeur de l'entier  a  :  "))
# b = int(input("Tapez la valeur de l'entier  b  :  "))
# q = a//b
# r = a%b
# print("Le quotient de la division euclidienne de a par b est  : q = ", q)
# print("Le reste de la division euclidienne de a par b est : r = ", r)


# # 14 - Lire la valeur de l'entier n
# n = int(input("Tapez la valeur de n :  "))
# # On utilise un compteur j 
# j = 0
# for i in range(0,n):
#     if(i**2 == n):
#         j = j +1
# if(j > 0):
#     print("L'entier  ", n , " est un carré parfait")
# else:
#     print("l'entier ", n , " n'est pas est un carré parfait")
