number1 = 420
number2 = 69
number3 = 666
day = "Mardi"
color = "caca d'oie"

print()

# partie 1

print("--- P1 ---")
if number1 > 0 :
    print("Le nombre est positif.")
elif number1 == 0 :
    print("Le nombre est égal à 0.")
else :
    print("Le nombre est négatif.")
print("----------")

print()
# partie 2

print("--- P2 ---")
if number1 % 2 == 0 :
    print("Le nombre est pair.")
else :
    print("Le nombre est impair.")
print("----------")

print()
# partie 3

print("--- P3 ---")
if number1 < number2 :
    print("Le nombre le plus petit est : " + str(number1))
else :
    print("Le nombre le plus petit est : " + str(number2))
print("----------")

print()
# partie 4

print("--- P4 ---")
if number1 > number2 and number1 > number3 :
    print("Le nombre le plus grand est : " + str(number1))
elif number2 > number1 and number2 > number3 :
    print("Le nombre le plus grand est : " + str(number2))
else:
    print("Le nombre le plus grand est : " + str(number3))

if number1 < number2 and number1 < number3 :
    print("Le nombre le plus petit est : " + str(number1))
elif number2 < number1 and number2 < number3 :
    print("Le nombre le plus petit est : " + str(number2))
else:
    print("Le nombre le plus grand est : " + str(number3))
print("----------")

print()
# partie 5

print("--- P5 ---")
if day == "Lundi" :
    print("C'est reparti !")
elif day == "Mercredi" :
    print("Jour des enfants.")
elif day == "Vendredi" :
    print("Bientôt le week-end !")
elif day == "Samedi" or day == "Dimanche" :
    print("Bon week-end <3")
else :
    print("Bonne semaine ;)")
print("----------")

print()
# partie 6

print("--- P6 ---")
if color == "rouge magenta" or color == "bleu cyan" or color == "jaune" :
    print("Couleurs primaires.")
elif color == "orange" or color == "violet" or color == "vert" :
    print("Couleurs secondaires.")
else :
    print("Autres couleurs.")
print("----------")

print()

