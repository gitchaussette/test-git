print()

print("--- V1 ---")
answer = input("Répondre oui ou non : ")
if answer == "oui" or answer == "non" :
    print("La réponse est " + answer + ".")
else :
    print("C'est une mauvaise réponse.")
print("----------")

print()


# partie 1

# Si on saisit "oui" en entrée, le programme retourne "La réponse est oui.".


# partie 2

# Si on saisit "non" en entrée, le programme retourne "La réponse est non.".


# partie 3

# Le programme demande d'écrire en entrée : "oui" ou "non".
# Si l'utilisateur entre "oui", le programme retourne "La réponse est oui.".
# Si l'utilisateur entre "non", le programme retourne "La réponse est non.".
# Sinon, si l'utilisateur n'écrit aucune des deux réponses demandées, le programme retourne "C'est une mauvaise réponse.".


# partie 4

print()

print("--- V2 ---")
answer = input("Répondre oui ou non : ")
if answer == "oui" or answer == "non" :
    print("La réponse est " + answer + ".")
else :
    print("C'est une mauvaise réponse.")

if len(answer) == 3 :
    print("La réponse est constituée de trois caractères.")
else :
    print("La réponse n'est pas constituée de trois caractères.")
print("----------")

print()