# # 1 - demander à l'utilisateur de saisir son nom
# name = input("Saisir votre nom : ")
# print("Bienvenue : " , name)

# # 2 - demander à l'utilisateur de saisir les valeurs de a et de b
# a = input("Tapez la valeur du nombre a : ")
# b = input("Tapez la valeur du nombre b : ")
# # Convertir les chaines de caractères en entier
# a = int(a)
# b = int(b)
# s = a+b
# print("La somme de a et de b est a + b = " , s)

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


# 7 - # Demander à l'utilisateur de taper 3 nombres  a, b, c
a = int(input("Type a value of the number a "))
b = int(input("Type a value of the number b "))
c = int(input("Type a value of the number c "))

# définir et initialiser le maximum à zero
max = 0
if(a > b and a > c):
    max = a
elif(b > c and b > a): 
    max = b
elif(c > a and c > b):
    max = c
else: 
    max = max
print("Le maximum des trois nombre est : max(a,b,c) = ", max)